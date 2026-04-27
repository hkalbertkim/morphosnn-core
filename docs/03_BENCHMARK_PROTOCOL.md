# Benchmark Protocol

## 1. Purpose

This protocol defines benchmark targets for body-near distributed control. It is intended to help evaluate local rhythm generation, sensory correction, prediction-error handling, sparse/event-like activity, and morphology-aware behavior.

## 2. Benchmark Status

This is a draft protocol for a seed repo, not a validated benchmark yet. Metrics and targets will need measured baselines before they can support performance claims.

## 3. Evaluation Axes

Initial evaluation axes include:

- latency;
- rhythm stability;
- sensory correction response;
- forward-model prediction error;
- spike/event activity proxy;
- morphology transfer;
- perturbation recovery;
- trajectory deviation;
- force/contact envelope violation;
- reproducibility.

## 4. Metrics Table

| Axis | Metric | Seed-stage measurement | Future validation target |
|---|---|---|---|
| Local response | controller update latency | toy runtime / simulated loop | physical sensor-to-actuator loop |
| Rhythm generation | phase stability | oscillator trace | robot rhythm stability |
| Sensory correction | correction response time | simulated perturbation | contact response latency |
| Forward model | prediction error | synthetic expected vs observed signal | physical state prediction error |
| Sparse activity | event/spike proxy count | software counter | SNN or neuromorphic activity log |
| Morphology adaptation | recovery after morphology change | simulation placeholder | modular/soft robot validation |
| Safety envelope | violation count | threshold simulation | force/contact threshold count |

## 5. Example Benchmark Flow

1. Define body graph.
2. Run local controller.
3. Introduce perturbation.
4. Log rhythm, correction, prediction error.
5. Compute metrics.
6. Compare to baseline.

## 6. Baselines

Candidate baselines include:

- naive oscillator;
- centralized controller placeholder;
- CPG baseline;
- future physical baseline.

Baseline definitions should be versioned and measured before claiming improvement.

## 7. Non-goals

This benchmark protocol does not claim:

- validated real-world performance yet;
- superiority without measured baseline;
- hardware-specific guarantee.

It is a public draft for organizing future benchmark work.
