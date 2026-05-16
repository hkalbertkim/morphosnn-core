# Toy CPG Controller

## What this example shows

This directory contains a minimal, dependency-free toy CPG oscillator example. It shows how two local rhythm channels can be represented as anti-phase signals before being mapped to richer SNN/CPG-style controller abstractions.

CPG-like rhythmic control is a useful first scaffold for locomotion-oriented task families because many walking, crawling, and legged-control primitives require repeatable phase relationships between local body channels.

## How to run

From the repository root:

```bash
python3 examples/toy_cpg_controller/cpg_oscillator.py
```

The script prints a short CSV-like terminal trace. It has no external dependencies.

## Expected output

The output starts with a header and then one row per timestep:

```text
time,left_signal,right_signal
0.00,0.0000,0.0000
0.10,0.3090,-0.3090
0.20,0.5878,-0.5878
0.30,0.8090,-0.8090
```

A reproducibility trace is included at [sample_output.csv](sample_output.csv).

## How to interpret the trace

- `time` is the simulated timestamp in seconds.
- `left_signal` is the sine output of the left rhythm channel.
- `right_signal` is the sine output of the right rhythm channel.
- The two channels are initialized in anti-phase, so positive values on one side correspond to negative values on the other side for much of the trace.

The example is intentionally small: it makes the rhythm primitive visible in text before adding richer body graphs, morphology-aware feedback, SNN implementations, or benchmark protocols.

## Scope boundaries / non-claims

This toy example is not:

- a full SNN model;
- a biological fidelity claim;
- a physical robot controller;
- a robotics benchmark;
- an energy benchmark;
- evidence of validated locomotion or physical adaptation.

It only illustrates rhythmic primitive generation that can later inform local SNN/CPG-style controller abstractions.

## How this connects to MorphoSNN

MorphoSNN studies morphology-coupled SNN and neuromorphic control starting from arthropod-inspired distributed body intelligence. Local rhythmic loops, reflex-like correction, and body-segment coordination are natural entry points for that research direction.

This example is the smallest runnable scaffold in the repository: it demonstrates an anti-phase rhythm primitive relevant to locomotion-oriented task families without claiming that the repository already contains a validated robot controller.
