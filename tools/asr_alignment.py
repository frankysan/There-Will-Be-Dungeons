"""Time-constrained phrase anchors followed by bounded edit alignment.

No speaker-label equivalence, majority voting, or synthetic word timestamps.
"""
from __future__ import annotations

from bisect import bisect_left, bisect_right
from collections import defaultdict


def bounds(words):
    times = [t for w in words for t in (w.start_ms, w.end_ms) if t is not None]
    return (min(times), max(times)) if times else (None, None)


def gap(a, b):
    if None in (a.start_ms, a.end_ms, b.start_ms, b.end_ms):
        return None
    return max(0, max(a.start_ms, b.start_ms) - min(a.end_ms, b.end_ms))


def nearby(a, b, drift):
    distance = gap(a, b)
    return distance is None or distance <= drift


def anchors(a, b, drift):
    """Unique local trigrams; LIS keeps ordered anchors, not global LCS words."""
    index = defaultdict(list)
    for j in range(len(b) - 2):
        if b[j].start_ms is not None:
            index[tuple(w.norm for w in b[j:j+3])].append((b[j].start_ms, j))
    for values in index.values():
        values.sort()
    widths = {key: max((abs(b[j].end_ms - b[j].start_ms) for _, j in values
                       if b[j].end_ms is not None), default=0) for key, values in index.items()}
    candidates = []
    for i in range(len(a) - 2):
        if a[i].start_ms is None or a[i].end_ms is None:
            continue
        key = tuple(w.norm for w in a[i:i+3])
        values = index.get(key, [])
        # Wide source cues retain coarse uncertainty; never interpolate them.
        lo = bisect_left(values, (a[i].start_ms - drift - widths.get(key, 0), -1))
        hi = bisect_right(values, (a[i].end_ms + drift, float('inf')))
        if hi - lo <= 64:  # Repetitive/very coarse passages defer to bounded alignment.
            matches = [j for _, j in values[lo:hi]
                       if all(nearby(x, y, drift) for x, y in zip(a[i:i+3], b[j:j+3]))]
            if len(matches) == 1:
                candidates.append((i, matches[0]))
    tails, nodes, parents = [], [], []
    for k, (_, j) in enumerate(candidates):
        pos = bisect_left(tails, j)
        parents.append(nodes[pos-1] if pos else -1)
        if pos == len(tails):
            tails.append(j)
            nodes.append(k)
        else:
            tails[pos], nodes[pos] = j, k
    chain = []
    k = nodes[-1] if nodes else -1
    while k >= 0:
        chain.append(candidates[k])
        k = parents[k]
    selected = []
    for i, j in reversed(chain):
        if not selected or (i >= selected[-1][0] + 3 and j >= selected[-1][1] + 3):
            selected.append((i, j))
    return selected


def edit(a, b, drift, stats):
    """Weighted edit path with 1:2/2:1 concatenation and explicit time gating."""
    n, m = len(a), len(b)
    stats['dp_cells'] += n * m
    stats['max_dp_cells'] = max(stats['max_dp_cells'], n * m)
    cost = [[0.0] * (m+1) for _ in range(n+1)]
    back = [[None] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        cost[i][0], back[i][0] = i, (1, 0, 'possible_omission')
    for j in range(1, m+1):
        cost[0][j], back[0][j] = j, (0, 1, 'possible_omission')
    for i in range(1, n+1):
        for j in range(1, m+1):
            x, y = a[i-1], b[j-1]
            options = [(cost[i-1][j]+1, (1, 0, 'possible_omission')),
                       (cost[i][j-1]+1, (0, 1, 'possible_omission'))]
            if nearby(x, y, drift):
                same = x.norm == y.norm
                # Prefer closer instances of repeated wording; intervals remain coarse.
                temporal = (gap(x, y) or 0) / max(1, drift) * .1
                options.insert(0, (cost[i-1][j-1] + (0 if same else 1.2) + temporal,
                                   (1, 1, 'agreement' if same else 'conflicting_recognition')))
                for di, dj in ((1, 2), (2, 1)):
                    if i >= di and j >= dj:
                        aa, bb = a[i-di:i], b[j-dj:j]
                        if (''.join(w.norm for w in aa) == ''.join(w.norm for w in bb)
                                and all(nearby(u, v, drift) for u in aa for v in bb)):
                            options.append((cost[i-di][j-dj]+.15,
                                            (di, dj, 'uncertain_segmentation')))
            cost[i][j], back[i][j] = min(options, key=lambda x: x[0])
    result = []
    i, j = n, m
    while i or j:
        di, dj, kind = back[i][j]
        result.append((kind, a[i-di:i], b[j-dj:j], []))
        i, j = i-di, j-dj
    return list(reversed(result))


def align(a, b, drift_ms=2000, max_tokens=192, window_ms=30000):
    if drift_ms < 0 or max_tokens < 4 or window_ms <= 0:
        raise ValueError('Invalid alignment bounds')
    stats = {'dp_cells': 0, 'max_dp_cells': 0, 'anchors': 0, 'fallback_blocks': 0}

    def bounded(aa, bb):
        if len(aa) <= max_tokens and len(bb) <= max_tokens:
            return edit(aa, bb, drift_ms, stats)
        # Temporal buckets retain every token. They can split shifted/cue-spanning
        # phrases, so every fallback operation is visibly uncertain, even equality.
        stats['fallback_blocks'] += 1
        buckets = defaultdict(lambda: [[], []])
        for side, words in enumerate((aa, bb)):
            for w in words:
                key = int(w.start_ms // window_ms) if w.start_ms is not None else -1
                buckets[key][side].append(w)
        out = []
        for key in sorted(buckets):
            xa, xb = buckets[key]
            for start in range(0, max(len(xa), len(xb)), max_tokens):
                ops = edit(xa[start:start+max_tokens], xb[start:start+max_tokens], drift_ms, stats)
                out.extend((kind, x, y, ['bounded_fallback: temporal/index partition may split speech'])
                           for kind, x, y, _ in ops)
        return out

    out, ai, bi = [], 0, 0
    selected = anchors(a, b, drift_ms)
    stats['anchors'] = len(selected)
    for i, j in selected:
        out.extend(bounded(a[ai:i], b[bi:j]))
        out.extend(('agreement', [a[i+k]], [b[j+k]], []) for k in range(3))
        ai, bi = i+3, j+3
    out.extend(bounded(a[ai:], b[bi:]))
    return out, stats
