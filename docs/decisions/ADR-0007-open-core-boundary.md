# ADR-0007: Open-Core Boundary

Status: Proposed

## Context

The public repository should be useful for documentation, examples, architecture, and benchmark scaffolding while avoiding private deployment details or partner-sensitive research material. Clear boundaries reduce the risk of accidentally publishing confidential or unpublished content.

## Decision

The public repo contains core concepts, examples, benchmarks, and documentation. Customer-specific deployment, private integration, partner-sensitive data, unpublished validation material, and proprietary hardware details remain outside the public core.

## Consequences

Public contributions should be reviewed for confidentiality and claim boundaries. Sensitive local materials should be ignored or stored outside the repository. Public examples should use generic data, toy systems, or cleared materials.

## Non-goals

The public core is not a place for partner-confidential data, private customer integrations, unpublished experimental results, or proprietary hardware design packages.
