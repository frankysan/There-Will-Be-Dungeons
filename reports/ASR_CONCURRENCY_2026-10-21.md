# Parallel CrispASR throughput observation (2026-10-21)

**Evidence status:** Archive owner's live observations, **not an instrumented or repeated benchmark**. This records pipeline throughput behavior, not transcription accuracy.

## Test description

- Two separate CrispASR processes running concurrently on the same Windows workstation.
- Hardware context: 32 GiB system RAM and AMD Radeon RX 9070 with 16 GB dedicated VRAM.
- Exact episode IDs, durations, model configuration, command lines, and single-process control-run times were **not supplied**. Do not equate this with the previously documented 600-second Parakeet tests or automatically assume the two episodes were identical in length.
- The owner reports both episodes complete in approximately **6–7 minutes each**, with **no obvious parallel slowdown**.

## Observed utilization (approximate)

| Resource / measure | Owner observation | Interpretation / caveat |
|---|---|---|
| System RAM | Nearly fully utilized | Likely concurrency constraint; used RAM alone does not distinguish committed working set from cache or reveal memory pressure |
| CPU | Well below saturation | Not obviously CPU-bound by overall reported utilization; does not rule out a serial bottleneck |
| GPU copy and compute | Peaks around 25% | Low reported engine-level utilization; measurement interval and scheduling details unknown |
| Dedicated VRAM | Around 8.5 GB of 16 GB | Headroom observed, but not evidence that another complete process would fit in system RAM |
| Disk | Essentially no activity | No sign of heavy disk paging during observation, though counters were not captured |
| Episode completion | ~6–7 minutes for each concurrent process | If both complete within the same 6–7-minute interval, combined rate is about 17–20 episodes per hour **of similar duration**. This rate is conditional and must not be generalized to other episode lengths |

## Preliminary conclusion

**Two concurrent CrispASR processes are a promising practical configuration on this machine.** The absence of noticeable slowdown and disk traffic is encouraging despite high system RAM consumption. A single-process sequential measurement on the same two files is still required to quantify throughput gain. Do not infer that GPU load alone justifies adding a third process.

## Follow-up benchmark

1. Record the two episode IDs, audio lengths, precise model/configuration and exact wall-clock durations from their tool logs.
2. Run the same two inputs **sequentially** using the identical settings; compare total wall time against concurrent total wall time, not against one file's time.
3. Capture minimum **available physical RAM**, system **committed bytes / commit limit**, disk hard-fault/page-read activity, GPU engine utilization and dedicated VRAM. Avoid posting private absolute paths or full environment dumps.
4. Recheck with different-length episodes and, when the multi-pass workflow is ready, a mixed **Parakeet + Qwen** pair. Model memory footprints may differ.
5. Keep concurrency configurable and conservatively default to two only where memory headroom and throughput are demonstrated on representative episodes.

**Do not use this throughput observation as evidence of recognition accuracy.** The multi-pass quality pilot requires separate audio-grounded review; see [multi-pass workflow](MULTIPASS_PIPELINE.md).
