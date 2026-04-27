# Physical AI Connection

## 1. Why Physical AI Needs Body-Near Control

Physical AI systems act through bodies. They must handle timing, contact, compliance, perturbation, sensing, and actuation constraints. These requirements motivate a body-near control layer below high-level planning.

## 2. Centralized Planning Is Not Enough

Centralized planning can define goals and strategies, but local interaction often requires faster correction and body-aware adaptation. A physical AI stack should make this layer explicit rather than hiding it inside a monolithic controller.

## 3. Local Rhythm Generation

Repeated movement can be organized through local rhythmic primitives. MorphoSNN uses CPG/SNN-inspired rhythm generation as an abstraction for local controller modules.

## 4. Reflex-Like Sensory Correction

Local sensory feedback can support reflex-like correction when perturbations, contact changes, or state mismatches occur. This is an engineering control pattern, not a biological realism claim.

## 5. Forward Models and Prediction Error

Forward models compare predicted and observed sensory outcomes. Prediction-error signals can help identify mismatch and guide local correction or logging.

## 6. Morphology as Part of Computation

Body mechanics can shape behavior. Compliance, geometry, passive dynamics, and contact can reduce or reshape the control burden, so validation should account for morphology.

## 7. MorphoSNN as a Control Layer

MorphoSNN is not a replacement for high-level AI planning. It is a body-near control layer intended to sit between planning and physical actuation.

## 8. Non-goals

MorphoSNN does not claim complete autonomy, guaranteed zero-shot adaptation, validated robotics performance, or hardware-specific deployment readiness at the seed stage.
