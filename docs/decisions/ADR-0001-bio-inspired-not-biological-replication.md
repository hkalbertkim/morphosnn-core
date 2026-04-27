# ADR-0001: Bio-Inspired, Not Biological Replication

Status: Proposed

## Context

MorphoSNN draws from biological motor-control concepts such as distributed ganglia, CPGs, sensory feedback, efference copy, neuromodulation, and morphological computation. These concepts are useful engineering references, but biological systems are complex and context-dependent. A public seed repository should avoid implying that MorphoSNN reproduces biological nervous systems directly.

## Decision

MorphoSNN uses biological systems as engineering abstraction, not one-to-one replication. Biological terms may be used to describe design inspiration, but implementation modules should be documented as control abstractions.

## Consequences

This keeps public claims conservative and easier to validate. It also allows the implementation to use practical engineering approximations without needing to prove biological fidelity. Documentation should distinguish inspiration, abstraction, implementation, and validated behavior.

## Non-goals

MorphoSNN is not a biological connectome simulation, a complete model of arthropod nervous systems, or a claim of biological equivalence.
