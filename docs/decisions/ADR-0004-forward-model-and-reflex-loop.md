# ADR-0004: Forward Model and Reflex Loop

Status: Proposed

## Context

Body-near control needs both prediction and correction. Efference copy and forward-model concepts motivate predicting sensory consequences of motor commands, while reflex-like loops motivate fast local correction from observed feedback.

## Decision

The architecture separates prediction/efference copy from reflex-like correction. Prediction-error signals should be represented explicitly rather than hidden inside one monolithic controller.

## Consequences

This separation makes controller behavior easier to inspect, test, and benchmark. It also supports future experiments that compare predicted and observed feedback without implying a complete world model.

## Non-goals

The forward model layer is not intended to be a full physical simulator, a complete state estimator, or proof of biological equivalence.
