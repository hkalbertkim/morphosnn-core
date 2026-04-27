# Biological Inspiration

## 1. Scope

MorphoSNN abstracts biological principles rather than reproducing biology. Biological terms are used as design references for engineering abstractions in distributed, body-near control.

The project does not claim biological realism, a validated biological model, or one-to-one replication of any nervous system.

## 2. Arthropod Distributed Motor Control

Arthropod nervous systems motivate distributed local control. Segmental ganglia and the ventral nerve cord provide a useful reference for thinking about local processing nodes connected through a communication backbone.

MorphoSNN maps this inspiration to modular controller components associated with body regions, sensors, actuators, and morphology.

## 3. Central Pattern Generators

Central pattern generators motivate rhythmic primitive generation for repeated motion. In MorphoSNN, CPGs inspire local rhythm modules that can produce oscillatory control patterns.

This is an engineering abstraction. The seed examples do not model biological CPG circuits.

## 4. Local Sensory Feedback

Mechanosensory and proprioceptive feedback motivate reflex-like correction close to the body. MorphoSNN treats local sensory feedback as a pathway for fast correction without requiring every adjustment to be decided by a centralized planner.

## 5. Efference Copy and Forward Models

Efference copy describes the use of a motor-command-related signal to predict expected sensory consequences. Forward models provide a high-level abstraction for comparing expected and observed feedback.

MorphoSNN maps this idea to prediction-error loops that can help local controllers identify mismatch, perturbation, or changing body-environment interaction.

## 6. Neuromodulation

Neuromodulation motivates global coordination without direct micromanagement of every actuator. In MorphoSNN, modulation signals can adjust local controller parameters, gains, coupling, or operating modes.

This is an engineering control abstraction, not a biochemical model.

## 7. Morphological Computation

Morphology, compliance, geometry, and body mechanics can reduce or reshape control burden. A body can contribute to control through passive dynamics, mechanical filtering, and structure-environment interaction.

MorphoSNN therefore treats validation as morphology-aware: controller behavior should be interpreted in relation to the body and task context.

## 8. Mapping Table

| Biological principle | Engineering abstraction | MorphoSNN component |
|---|---|---|
| Segmental ganglia | Local processing node | Local CPG / SNN Controller |
| Ventral nerve cord | Distributed communication backbone | Body Graph Layer |
| CPG | Rhythmic primitive generator | Local CPG Block |
| Mechanosensory feedback | Event-like sensory correction | Sensory Reflex Loop |
| Efference copy | Predicted sensory consequence | Forward Model Layer |
| Neuromodulation | Global parameter modulation | Global Coordination Layer |
| Body mechanics | Physical contribution to control | Morphology-Aware Validation |

## 9. Non-goals

MorphoSNN does not claim:

- one-to-one biological replication;
- biological realism;
- a validated biological model.

The biological references are used to guide public engineering design, not to assert biological equivalence.
