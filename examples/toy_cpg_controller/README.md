# Toy CPG Controller

## Purpose

This directory contains a minimal, dependency-free illustration of rhythmic primitive generation. It is intended to make the CPG/SNN controller abstraction concrete without claiming biological realism or robotics validation.

## How to Run

From the repository root:

```bash
python3 examples/toy_cpg_controller/cpg_oscillator.py
```

The script prints a short time-series of two coupled anti-phase rhythm signals.

## What It Demonstrates

- A tiny oscillator state updated over time.
- Two rhythm channels with anti-phase coupling.
- A simple text output format that can be inspected without plotting libraries.

## What It Does Not Demonstrate

This toy example is not a biological simulation and not a robot controller. It only illustrates the idea of rhythmic primitive generation that can later be mapped into local SNN/CPG-style controller abstractions.

It does not demonstrate validated locomotion, morphology-aware benchmarking, zero-shot transfer, or physical adaptation.
