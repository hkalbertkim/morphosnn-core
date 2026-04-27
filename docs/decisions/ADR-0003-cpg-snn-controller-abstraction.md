# ADR-0003: CPG / SNN Controller Abstraction

Status: Proposed

## Context

Repeated physical behaviors often benefit from rhythmic primitives. CPG concepts provide a useful way to think about local rhythm generation, while SNNs provide an implementation direction for event-based or neuromorphic control.

## Decision

Local controllers are modeled as CPG/SNN-inspired rhythmic primitive generators. Early seed examples may use simple oscillators to illustrate the abstraction before introducing richer SNN implementations.

## Consequences

The project can separate conceptual controller behavior from implementation detail. Toy examples should be labeled clearly as illustrations, not biological simulations or robot controllers. Future interfaces should support local controller state, coupling, parameters, and outputs.

## Non-goals

The CPG/SNN abstraction does not claim biological realism, validated locomotion, or guaranteed transfer to arbitrary robot morphologies.
