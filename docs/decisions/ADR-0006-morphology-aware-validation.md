# ADR-0006: Morphology-Aware Validation

Status: Proposed

## Context

Controller behavior depends on body structure, compliance, actuation, sensing, and passive dynamics. Evaluating a controller without accounting for morphology can hide important assumptions and overstate generality.

## Decision

Validation should account for morphology, compliance, and physical embodiment. Benchmark records should document the body model, assumptions, metrics, and limits of each result.

## Consequences

MorphoSNN should avoid broad claims from narrow tests. Seed-stage materials can define validation pathways and benchmark targets, but should not claim validated robotics performance until evidence exists.

## Non-goals

Morphology-aware validation does not imply a validated industrial robotics benchmark, universal transfer, or guaranteed zero-shot performance.
