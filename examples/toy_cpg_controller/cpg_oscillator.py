#!/usr/bin/env python3
"""Toy anti-phase oscillator for illustrating rhythmic primitives.

This is not a biological simulation and not a robot controller. It is a
dependency-free sketch of how two local rhythm channels can be represented in a
small example before being mapped to richer SNN/CPG-style abstractions.
"""

from __future__ import annotations

import math


def wrap_phase(phase: float) -> float:
    """Keep a phase value in [0, 2*pi)."""
    return phase % (2.0 * math.pi)


def step_phase(phase: float, neighbor: float, omega: float, coupling: float, dt: float) -> float:
    """Advance one oscillator with weak anti-phase coupling."""
    target_offset = math.pi
    phase_error = math.sin((neighbor - phase) - target_offset)
    return wrap_phase(phase + dt * (omega + coupling * phase_error))


def main() -> None:
    dt = 0.1
    omega = 2.0 * math.pi * 0.5
    coupling = 0.8
    steps = 40

    left_phase = 0.0
    right_phase = math.pi

    print("time,left_signal,right_signal")
    for index in range(steps + 1):
        time = index * dt
        left_signal = math.sin(left_phase)
        right_signal = math.sin(right_phase)
        print(f"{time:.2f},{left_signal:.4f},{right_signal:.4f}")

        next_left = step_phase(left_phase, right_phase, omega, coupling, dt)
        next_right = step_phase(right_phase, left_phase, omega, coupling, dt)
        left_phase, right_phase = next_left, next_right


if __name__ == "__main__":
    main()
