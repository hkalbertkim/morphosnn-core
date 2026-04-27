<p align="center">
  <img src="assets/Main_logo_img_and_txt.png" alt="MorphoSNN logo" width="520">
</p>

<p align="center">
  <img alt="status: seed repo" src="https://img.shields.io/badge/status-seed%20repo-6b7280">
  <img alt="license: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-2563eb">
  <img alt="field: Physical AI" src="https://img.shields.io/badge/field-Physical%20AI-059669">
  <img alt="paradigm: Bio-inspired SNN" src="https://img.shields.io/badge/paradigm-Bio--inspired%20SNN-7c3aed">
  <img alt="focus: Distributed Control" src="https://img.shields.io/badge/focus-Distributed%20Control-f97316">
  <a href="https://github.com/hkalbertkim/morphosnn-core/releases/tag/v0.1.0-seed">
    <img src="https://img.shields.io/badge/release-v0.1.0--seed-23384d" alt="release">
  </a>
</p>

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README.ko.md">한국어</a>
</p>

<h3 align="center">Bio-inspired Distributed Neuromorphic Physical AI</h3>

## Overview

MorphoSNN is a bio-inspired distributed neuromorphic control stack for physical AI.

MorphoSNN focuses on the missing body-near intelligence layer between high-level AI planning and physical actuation: local rhythm generation, reflex-like sensory correction, neuromodulation, and morphology-aware adaptation.

The project uses biomimetic design principles, but does not attempt to reproduce biological nervous systems one-to-one. Instead, it abstracts distributed motor-control principles from arthropod nervous systems—segmental ganglia, central pattern generators, sensory feedback, efference copy, neuromodulation, and morphological computation—into modular SNN-based control architectures.

## Why MorphoSNN

Modern AI systems are increasingly capable of high-level perception, planning, and decision-making, but physical systems still need fast, local, body-aware control. MorphoSNN treats this body-near layer as a first-class design problem rather than a low-level implementation detail.

The seed repository organizes the concepts, architecture, examples, and research notes needed to develop that layer in a public, implementation-ready form.

## Core Thesis

Physical AI benefits from distributed control modules that are close to the body, coupled through morphology, and modulated by higher-level context. In MorphoSNN, local rhythmic primitives, sensory correction, forward prediction, and morphology-aware validation are treated as complementary parts of one neuromechanical control stack.

## Architecture

| Layer | Role |
|---|---|
| Body Graph Layer | Represents modules, sensors, actuators, and morphology |
| Local CPG / SNN Controller Layer | Generates local rhythmic primitives |
| Sensory Reflex Loop Layer | Performs reflex-like sensory correction |
| Forward Model / Efference Copy Layer | Compares predicted and observed sensory outcomes |
| Neuromodulation / Global Coordination Layer | Modulates local controllers without micromanaging every actuator |
| Morphology-Aware Validation Layer | Connects control outputs to physical morphology and benchmarks |

## Scientific Foundations

MorphoSNN is informed by distributed motor-control ideas from arthropod nervous systems, central pattern generators, sensory feedback loops, efference copy, neuromodulation, and morphological computation.

These ideas are used as engineering abstractions. The project does not claim biological fidelity, validated robotics performance, or guaranteed transfer across arbitrary bodies.

## Start Here

| Goal | Read |
|---|---|
| Understand the project thesis | [docs/00_CONCEPT.md](docs/00_CONCEPT.md) |
| Understand the architecture | [docs/01_ARCHITECTURE.md](docs/01_ARCHITECTURE.md) |
| Understand the biological basis | [docs/02_BIOLOGICAL_INSPIRATION.md](docs/02_BIOLOGICAL_INSPIRATION.md) |
| Understand benchmark direction | [docs/03_BENCHMARK_PROTOCOL.md](docs/03_BENCHMARK_PROTOCOL.md) |
| Understand validation pathway | [docs/04_EPFL_RRL_VALIDATION.md](docs/04_EPFL_RRL_VALIDATION.md) |
| Understand roadmap | [docs/05_ROADMAP.md](docs/05_ROADMAP.md) |
| Read the seed specification | [SPEC.md](SPEC.md) |
| Read design decisions | [docs/decisions/](docs/decisions/) |
| Run the toy example | [examples/toy_cpg_controller/](examples/toy_cpg_controller/) |
| Review references | [research/bibliography/references.md](research/bibliography/references.md) |

## Repository Structure

- [assets/](assets/) - Project logos and visual assets.
- [docs/](docs/) - Concept, architecture, validation, benchmark, roadmap, and design-decision documentation.
- [research/](research/) - Public research notes, conceptual slide materials, and bibliography scaffolding.
- [examples/](examples/) - Minimal runnable examples that illustrate core abstractions.
- [benchmarks/](benchmarks/) - KPI tables and benchmark protocol artifacts.
- [paper/](paper/) - Technical note and publication-oriented drafts.

## Current Status

MorphoSNN Core is currently a seed reference repository. It contains public concept documents, a seed specification, design decision records, scientific foundation notes, a draft benchmark protocol, and a toy CPG example. It is not yet a validated robotics benchmark or deployment-ready control stack.

The toy CPG oscillator includes a reproducible sample output trace at [examples/toy_cpg_controller/sample_output.csv](examples/toy_cpg_controller/sample_output.csv).

## Non-goals

MorphoSNN is currently a seed reference stack. It does not claim to:

- reproduce biological nervous systems one-to-one;
- provide a validated robotics benchmark yet;
- guarantee zero-shot or few-shot adaptation across arbitrary physical systems;
- include partner-specific confidential data, unpublished results, or proprietary hardware designs;
- replace high-level AI planning systems. MorphoSNN focuses on the body-near control layer between high-level planning and physical actuation.

## Roadmap

- Refine the body graph and local controller interfaces.
- Expand the toy CPG example into a small testable controller abstraction.
- Populate the bibliography with primary scientific and technical references.
- Define benchmark metrics before claiming robotics validation.
- Keep public core materials separated from private deployments and partner-sensitive research.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
