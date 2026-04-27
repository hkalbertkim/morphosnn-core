# ADR-0005: Neuromodulation as Global Coordination

Status: Proposed

## Context

Distributed local controllers need coordination without requiring a central process to command every actuator at every step. Neuromodulation provides a useful inspiration for changing controller mode, gain, coupling, rhythm, or responsiveness at a global or regional level.

## Decision

Global coordination modulates local controllers rather than directly commanding every actuator. Modulation signals should affect parameters or operating modes while preserving local control responsibilities.

## Consequences

The architecture can support centralized context without collapsing into centralized micromanagement. Benchmarks should distinguish local controller outputs from modulation effects.

## Non-goals

Neuromodulation in MorphoSNN is an engineering abstraction. It is not a biochemical model, a guarantee of robust adaptation, or a replacement for task planning.
