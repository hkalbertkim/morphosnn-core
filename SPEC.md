# MorphoSNN Core Specification

This is a seed specification. It defines initial public concepts and boundaries for `morphosnn-core`; it is not a final standard or a validated robotics benchmark.

## 1. Purpose

MorphoSNN Core specifies a bio-inspired distributed neuromorphic control stack for physical AI. Its purpose is to organize body-near control abstractions that sit between high-level AI planning and physical actuation.

## 2. Scope

The core scope includes architecture, terminology, minimal examples, benchmark targets, and public research scaffolding. The repository may include toy examples and conceptual materials, but it should not include partner-confidential data, proprietary hardware details, or unpublished validation results.

## 3. Problem Definition

Physical AI systems often need more than high-level plans and actuator commands. They also need local rhythm generation, fast sensory correction, predictive feedback, and morphology-aware adaptation near the body. MorphoSNN addresses this intermediate control layer as a modular, distributed system.

## 4. Scientific Basis

MorphoSNN uses biological systems as sources of engineering abstraction. The project does not attempt one-to-one biological replication.

### 4.1 Arthropod Distributed Motor Control

Arthropod motor systems motivate distributed control, segment-local processing, and body-part-specific coordination. MorphoSNN abstracts these principles into local controller modules mapped to a body graph.

### 4.2 Central Pattern Generators

Central pattern generators motivate rhythmic primitive generation for repeated motion. In MorphoSNN, CPG-like behavior is represented as an engineering abstraction that may later be implemented with SNN modules.

### 4.3 Local Sensory Feedback and Reflex-Like Correction

Local feedback pathways motivate fast correction close to sensors and actuators. MorphoSNN treats reflex-like correction as a control design pattern, not as a claim of biological equivalence.

### 4.4 Efference Copy and Forward Models

Efference copy and forward models motivate comparing expected sensory outcomes with observed feedback. This supports prediction-error signals that can inform local adjustment and validation.

### 4.5 Neuromodulation

Neuromodulation motivates global or regional changes to controller mode, gain, coupling, and rhythm. MorphoSNN uses this idea to coordinate local modules without micromanaging every actuator.

### 4.6 Morphological Computation

Morphological computation motivates treating body mechanics, compliance, geometry, and passive dynamics as part of the control problem. MorphoSNN validation should account for morphology rather than evaluating controllers in isolation.

## 5. System Architecture

MorphoSNN is organized around six layers.

### 5.1 Body Graph Layer

Represents body modules, segments, joints, sensors, actuators, and topology. It defines where local controllers attach and how signals are routed.

### 5.2 Local CPG / SNN Controller Layer

Generates local rhythmic primitives and controller states. Early examples may use simple oscillators; later implementations may use SNN-based controller modules.

### 5.3 Sensory Reflex Loop Layer

Processes local sensory feedback and applies reflex-like correction. This layer should remain explicit so correction is not hidden inside high-level planning.

### 5.4 Forward Model / Efference Copy Layer

Tracks expected consequences of motor commands and compares them with observed sensory feedback. The output is a prediction-error signal, not a complete world model.

### 5.5 Neuromodulation / Global Coordination Layer

Applies global or regional modulation to local controllers. It may adjust gains, frequencies, coupling, or operating modes without commanding every actuator directly.

### 5.6 Morphology-Aware Validation Layer

Evaluates behavior in relation to body structure, passive dynamics, task context, and benchmark metrics. At the seed stage, this layer defines validation direction rather than validated performance claims.

## 6. Inputs and Outputs

Typical inputs include body graph definitions, local sensor streams, controller parameters, modulation signals, and task context. Typical outputs include rhythmic control signals, local correction signals, prediction-error traces, and benchmark measurements.

## 7. Core Data Structures

- Body graph: nodes for body modules and edges for mechanical or signal relationships.
- Controller module: local rhythm generator with state, parameters, and outputs.
- Sensor channel: typed feedback stream associated with a body graph location.
- Reflex rule: local mapping from sensory state to correction signal.
- Forward model state: expected sensory outcome and prediction error.
- Modulation signal: global or regional parameter update.
- Validation record: benchmark context, metrics, assumptions, and results.

## 8. Benchmark Targets

Initial benchmark targets should measure controllability, rhythm stability, local correction behavior, energy or actuation cost where available, robustness to bounded perturbations, and morphology-aware task performance. These targets are proposed directions, not validated benchmark results.

## 9. Validation Pathway

Validation should progress from toy oscillator examples, to simulated body graphs, to morphology-aware benchmark protocols, and only then to physical experiments where appropriate. Claims should remain tied to the tested setting and should not imply guaranteed transfer to arbitrary robots.

## 10. Non-goals

MorphoSNN does not aim to be:
- a biological connectome simulation;
- a complete robot autonomy stack;
- a guaranteed zero-shot adaptation system;
- a validated industrial robotics benchmark at the seed-repo stage;
- a repository for partner-confidential or unpublished validation data.

## 11. Roadmap

- Define minimal body graph and controller interfaces.
- Add a small testable CPG-style controller abstraction.
- Expand benchmark protocol and KPI tables.
- Populate bibliography with primary literature.
- Document morphology-aware validation scenarios and claim boundaries.
