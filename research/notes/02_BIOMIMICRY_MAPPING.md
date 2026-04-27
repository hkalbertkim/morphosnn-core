# Biomimicry Mapping

## 1. Mapping Principle

MorphoSNN uses biomimicry as a design method for engineering abstractions. Biological references are mapped to software and control components only where they clarify the architecture.

The mapping is intentionally cautious: inspiration does not imply biological fidelity.

## 2. Mapping Table

| Biological reference | Engineering abstraction | MorphoSNN component | Seed repo artifact |
|---|---|---|---|
| Segmental ganglia | Local processing node | Local CPG / SNN controller | toy CPG example |
| Ventral nerve cord | Distributed backbone | Body graph layer | SPEC / architecture docs |
| CPG | Rhythmic primitive generator | Local rhythm block | cpg_oscillator.py |
| Mechanoreceptors | Event-like sensory correction | Sensory reflex loop | benchmark protocol |
| Reflex reversal | Phase-dependent routing | Reflex control policy | future simulation |
| Efference copy | Predicted sensory outcome | Forward model layer | SPEC placeholder |
| Neuromodulation | Global parameter modulation | Coordination layer | ADR-0005 |
| Body mechanics | Physical computation | Morphology-aware validation | validation pathway docs |

## 3. What Is Abstracted

MorphoSNN abstracts:

- local processing;
- distributed coordination;
- rhythmic primitive generation;
- event-like sensory correction;
- prediction-error loops;
- global parameter modulation;
- body mechanics as part of control.

## 4. What Is Not Claimed

MorphoSNN does not claim biological realism, a complete biological model, one-to-one replication, or validated robotics performance. The mapping is a public design scaffold for future implementation and benchmarks.
