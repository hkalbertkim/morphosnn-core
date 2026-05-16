# Neural Manifold Alignment

## Purpose

This document defines the RFP-oriented technical layer for MorphoSNN. The proposed framing is to quantify Biological Neural Manifold representation structure through mathematical and geometric analysis, then compare those structures with ANN and SNN representation spaces using alignment and similarity metrics.

The goal is to support interpretable and efficient next-generation AI design and optimization. At the current seed stage, this is a proposed metric path and reference-stack direction, not a validated implementation claim.

```mermaid
flowchart LR
    A[Biological Neural Manifold] --> B[Geometry Metrics]
    B --> C[ANN/SNN Representation Alignment]
    C --> D[Task-Efficiency Relations]
    D --> E[MorphoSNN Reference Stack]
    E --> F[Robotics Task-Family Benchmark]
```

## What Is Being Quantified

The central object is the geometry of neural or model representations under task conditions. For biological systems, this may mean population activity trajectories, task-conditioned latent spaces, or state-dependent response manifolds. For ANN and SNN systems, this may mean hidden activations, spike-event traces, latent state trajectories, controller states, or learned policy representations.

MorphoSNN treats these representations as objects for engineering analysis. The project does not claim biological fidelity or one-to-one replication of nervous systems.

## Candidate Geometry Metrics

| Metric family | What it measures | Possible biological source | Possible ANN/SNN counterpart | Why it matters for design/optimization |
|---|---|---|---|---|
| Intrinsic dimensionality | Effective latent degrees of freedom used during a task | Neural population activity across task states | Hidden activations, spike-state embeddings, controller latent states | Helps estimate compactness, redundancy, and control-relevant state size |
| Trajectory geometry | Shape, speed, recurrence, and organization of state trajectories | Population trajectories during movement or sensory response | ANN hidden-state paths, SNN spike-state trajectories, CPG phase traces | Helps compare dynamic structure and task-conditioned state evolution |
| Separability / class or state margin | How clearly task states, actions, or conditions separate in representation space | State-labeled population activity | Classifier margins, policy-state separability, latent clustering | Supports robustness, decoding, and simpler downstream control |
| Curvature or local smoothness | Local geometric regularity and sensitivity to small state changes | Smoothness of neural trajectories or manifold neighborhoods | Activation-manifold curvature, local Jacobian behavior, spike-state transitions | Helps identify stable and interpretable regions for control |
| Stability under perturbation | Whether representations remain coherent under noise or physical disturbance | Perturbed sensory or motor trials | Noisy inputs, morphology shifts, actuator perturbation traces | Connects representation geometry to robustness and recovery |
| Representation similarity / alignment | Degree of structural correspondence across systems or conditions | Cross-animal, cross-task, or cross-region activity patterns | ANN/SNN layer comparisons, trained-model comparisons, biological-model comparisons | Enables translation from biological geometry hypotheses to model design metrics |
| Sparsity / event activity proxy | Activity concentration, event rate, or inactive-state structure | Sparse neural firing or event timing patterns | SNN spike counts, event rates, sparse activations | Provides a proxy for computation and energy efficiency |
| Task-efficiency relation proxy | Relationship between geometry and task-level efficiency | Behavior-linked neural activity under varied task demands | Generalization, sample complexity, compute cost, robustness, local adaptation | Tests whether geometry metrics provide useful design guidance |

## ANN/SNN Representation Alignment

Candidate alignment methods include centered kernel alignment, representational similarity analysis, and Procrustes-style representation similarity. These methods are listed as metric families to evaluate, not as implemented MorphoSNN features at the seed stage.

Possible comparisons include:

- biological population geometry versus SNN state trajectories;
- ANN hidden representation geometry versus SNN event-state geometry;
- controller representations before and after perturbation;
- task-efficient and task-inefficient model variants;
- local body-near controllers under different morphology conditions.

## From Alignment to Design/Optimization

The intended design loop is:

1. Quantify candidate biological representation geometry.
2. Measure whether ANN or SNN models show related geometric structure.
3. Relate that structure to task-efficiency signals such as generalization, sample complexity, computation or energy proxy, robustness, and local adaptation.
4. Convert useful relationships into open-source reference-stack components, benchmark protocols, and design guidelines.

The engineering value is not the claim that a model is biologically faithful. The value is whether representation geometry gives measurable, reproducible guidance for building more interpretable and efficient AI controllers.

## Current Seed Status and Non-Claims

MorphoSNN currently provides public concept documents, a toy CPG example, benchmark scaffolding, and claim boundaries. It does not yet provide validated neural-manifold metrics, implemented CKA/RSA/Procrustes pipelines, confirmed biological datasets, or validated robotics performance.

This document should be treated as a proposed RFP-oriented technical framing. It does not claim biological fidelity, confidential data access, partner-specific validation, or completed benchmark results.
