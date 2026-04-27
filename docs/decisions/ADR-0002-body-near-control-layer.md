# ADR-0002: Body-Near Control Layer

Status: Proposed

## Context

High-level AI planning can specify goals, constraints, and task context, but physical systems also require local control close to sensors, actuators, and body mechanics. This layer is where rhythm generation, reflex-like correction, and morphology-aware adaptation can be handled before every detail reaches a centralized planner.

## Decision

MorphoSNN focuses on the control layer between high-level AI planning and physical actuation. The project treats body-near control as a distinct architectural concern.

## Consequences

Interfaces should separate high-level task context from local control state. Examples and benchmarks should make clear whether they exercise planning, body-near control, or physical validation. This keeps the core scope narrower than a complete autonomy stack.

## Non-goals

MorphoSNN does not replace high-level AI planning systems and does not define a full robot autonomy pipeline.
