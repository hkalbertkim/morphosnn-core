# MorphoSNN Core Specification

## 1. Scope

MorphoSNN Core defines a bio-inspired distributed neuromorphic control stack for physical AI systems. The core specification covers architecture, abstractions, validation expectations, and public repository boundaries.

## 2. Design Position

MorphoSNN is bio-inspired but does not attempt biological replication. It abstracts distributed motor-control principles into engineering modules suitable for SNN-based control systems.

## 3. Core Architecture

The initial architecture is organized around six layers:

1. Body Graph Layer
2. Local CPG / SNN Controller Layer
3. Sensory Reflex Loop Layer
4. Forward Model / Efference Copy Layer
5. Neuromodulation / Global Coordination Layer
6. Morphology-Aware Validation Layer

## 4. Core Abstractions

- Body graph: representation of morphology, segments, sensors, and actuators.
- Controller module: local SNN or CPG-inspired unit mapped to part of the body graph.
- Reflex loop: fast sensory correction pathway.
- Efference copy: expected sensory consequence of motor output.
- Neuromodulatory signal: global or regional coordination input.
- Validation task: morphology-aware evaluation setting with explicit metrics.

## 5. Validation Expectations

Validation should separate controller behavior, morphology effects, and task performance. Benchmark artifacts should define metrics, baselines, assumptions, and reproducibility requirements.

## 6. Open-Core Boundary

The public core repository should contain architecture, documentation, examples, benchmark protocols, and non-sensitive conceptual materials. Partner-sensitive, unpublished, or restricted validation material should remain outside the public commit history until cleared.

## 7. Roadmap

- Define minimal body graph and controller interfaces.
- Add toy CPG controller example.
- Expand benchmark protocol and KPI table.
- Populate bibliography with primary literature.
- Document morphology-aware validation scenarios.

## 10. Non-goals

MorphoSNN does not aim to be:
- a biological connectome simulation;
- a complete robot autonomy stack;
- a guaranteed zero-shot adaptation system;
- a validated industrial robotics benchmark at the seed-repo stage;
- a repository for partner-confidential or unpublished validation data.
