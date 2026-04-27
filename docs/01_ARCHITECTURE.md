# MorphoSNN Architecture

MorphoSNN is organized as a layered body-near control stack. The architecture separates embodied structure, local rhythm generation, sensory correction, predictive feedback, global coordination, and validation against physical morphology.

## Six-Layer Architecture

1. Body Graph Layer
2. Local CPG / SNN Controller Layer
3. Sensory Reflex Loop Layer
4. Forward Model / Efference Copy Layer
5. Neuromodulation / Global Coordination Layer
6. Morphology-Aware Validation Layer

## Layer Notes

The Body Graph Layer represents the physical morphology, joints, segments, sensors, and actuator topology. It provides the structural substrate for local controller placement.

The Local CPG / SNN Controller Layer generates rhythmic activity through modular spiking controllers that can be composed across body segments.

The Sensory Reflex Loop Layer provides fast local correction using proprioceptive, tactile, or other body-near signals.

The Forward Model / Efference Copy Layer tracks expected sensory consequences of motor commands and supports local prediction-error handling.

The Neuromodulation / Global Coordination Layer adjusts controller gains, modes, rhythms, and coupling patterns across distributed modules.

The Morphology-Aware Validation Layer evaluates controller behavior in relation to body mechanics, morphology, and physical task constraints.
