"""Exact, audio-unverified inter-ASR text metrics shared by episode tooling.

Keep this normalization independent of time-aware candidate alignment, whose
normalization and scoring answer a different question.
"""

def tokens(text):
    """Lowercase; join apostrophes; split on non-Unicode letters and digits."""
    text = text.lower().replace("'", '').replace('’', '')
    return ''.join(c if c.isalpha() or c.isdigit() else ' ' for c in text).split()


def distance(a, b):
    """Exact ordered unit-cost word Levenshtein via unbounded bit vectors.

    Inputs are sequences of normalized tokens. This is inter-model disagreement,
    never audio-verified WER or evidence that either model is correct.
    """
    if len(a) > len(b):
        a, b = b, a
    if not a:
        return len(b)
    masks = {}
    for i, word in enumerate(a):
        masks[word] = masks.get(word, 0) | (1 << i)
    positive, negative, score = ~0, 0, len(a)
    high = 1 << (len(a) - 1)
    for word in b:
        equal = masks.get(word, 0)
        vertical = equal | negative
        horizontal = (((equal & positive) + positive) ^ positive) | equal
        plus = negative | ~(horizontal | positive)
        minus = positive & horizontal
        score += bool(plus & high) - bool(minus & high)
        plus = (plus << 1) | 1
        minus <<= 1
        positive = minus | ~(vertical | plus)
        negative = plus & vertical
    return score
