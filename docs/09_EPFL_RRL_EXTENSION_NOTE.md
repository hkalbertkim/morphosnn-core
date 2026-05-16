# EPFL RRL Extension Note

## Purpose

This note clarifies how MorphoSNN can relate to EPFL/RRL-style robotics directions in public-safe terms.

## Embodied Validation Context

EPFL/RRL-style modular, origami, and soft robotics provides a strong embodied validation context for testing distributed control, morphology-aware adaptation, and physical perturbation recovery.

Existing task-conditioned morphology/control planning and LLM-based embodiment planning directions can be viewed as complementary high-level planning and design layers. They can help define goals, body plans, task conditions, or adaptation strategies.

## MorphoSNN Layer

MorphoSNN adds a body-near neuromorphic layer focused on:

- local sensing;
- rhythm generation;
- reflex correction;
- prediction error;
- morphology-aware feedback;
- ANN/SNN representation alignment.

This layer is intended to operate between high-level planning and physical actuation. It does not replace planning systems.

## Public-Safe Claim Boundary

MorphoSNN does not claim current partner-specific validation, confidential data access, or confirmed funded EPFL/RRL participation.

The proposed pathway is to test whether neural-manifold-inspired geometry can support interpretable and efficient distributed control under physical variation. Robotics is the first constrained validation family, not the final application boundary.
