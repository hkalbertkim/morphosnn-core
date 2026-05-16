# Demo Readiness Guide

## Purpose

This guide helps a visitor, reviewer, or presenter walk through MorphoSNN quickly before a short presentation or evaluation discussion. It keeps the focus on what the public repository currently shows and what it does not yet claim.

## 2-minute walkthrough

1. Open [README.md](../README.md) and show the one-line project definition.
2. Point to the full visual concept story in [10_NEUROMORPHIC_STRATEGIC_THESIS.md](10_NEUROMORPHIC_STRATEGIC_THESIS.md).
3. Open the toy CPG example guide at [examples/toy_cpg_controller/README.md](../examples/toy_cpg_controller/README.md).
4. Run `python3 examples/toy_cpg_controller/cpg_oscillator.py`.
5. Explain that the script is an early rhythmic-control scaffold, not a full SNN model or robot controller.

## What to show first

Start with the top of [README.md](../README.md): logo, one-line definition, problem / thesis / current-repo bullets, and the current non-claims note. Then use [docs/README.md](README.md) as the documentation map.

## Run the toy CPG example

From the repository root:

```bash
python3 examples/toy_cpg_controller/cpg_oscillator.py
```

Expected representative output:

```text
time,left_signal,right_signal
0.00,0.0000,0.0000
0.10,0.3090,-0.3090
0.20,0.5878,-0.5878
0.30,0.8090,-0.8090
```

## What the output means

- `time` is the simulated timestamp in seconds.
- `left_signal` is the left rhythm-channel output.
- `right_signal` is the right rhythm-channel output.
- The two rhythm channels are initialized in anti-phase, which makes the trace useful as a minimal locomotion-oriented rhythm scaffold.

## What this repository currently demonstrates

- Public README positioning: done.
- Strategic thesis / visual story: available.
- Toy CPG example: runnable.
- Physical robot integration: not yet.
- Full SNN benchmark: not yet.
- Energy benchmark: not yet.

## What this repository does not claim

MorphoSNN does not claim biological fidelity, production readiness, robotics benchmarking, general SNN superiority, official validation, measured energy reduction, or an AlexNet-level achievement.

The toy CPG example is a minimal educational and research scaffold. It is not a physical robot controller, a full SNN implementation, or an energy benchmark.

## Useful links

- [Main README](../README.md)
- [Korean README](../README.ko.md)
- [Documentation map](README.md)
- [Neuromorphic strategic thesis](10_NEUROMORPHIC_STRATEGIC_THESIS.md)
- [Toy CPG example guide](../examples/toy_cpg_controller/README.md)
- [Toy CPG script](../examples/toy_cpg_controller/cpg_oscillator.py)
