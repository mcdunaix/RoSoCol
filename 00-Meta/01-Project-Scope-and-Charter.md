---
title: Project Scope and Charter
tags: [meta, scope, charter]
created: 2026-10-06
status: active
---

# Project Scope and Charter: RoSoCol

## 1. Problem Statement

Conventional concentrated solar power (CSP) and concentrated photovoltaics (CPV) require dual-axis mechanical tracking systems to maintain alignment with direct normal irradiance (DNI). Mechanical trackers introduce parasitic power consumption, failure modes from gears and actuators, wind-load vulnerability, and elevated capital expenditure (CapEx).

The Rotational Omnidirectional Solar Collector (RoSoCol) aims to eliminate active tracking through stationary non-imaging optics with rotational symmetry, concentrating solar radiation across continuous diurnal azimuthal arcs and seasonal elevation shifts.

## 2. Core Objectives

1. Design a stationary or semi-static optical concentrator operating over an azimuthal span $\Delta\phi = 360^\circ$.
2. Maintain effective geometric concentration $C_g \ge 1.5\times$ to $3.0\times$ without continuous mechanical tracking.
3. Quantify optical efficiency $\eta_{\text{opt}}$ and skew-ray losses using Monte Carlo ray tracing.
4. Establish trade-offs between acceptance angle, solid dielectric mass, and thermal dissipation on the receiver.

## 3. Physical Boundary Conditions

- **Conservation of Étendue**: Hemispherical acceptance ($\theta_{\text{in}} = 90^\circ$) yields a theoretical maximum concentration $C \le 1.0$ in air ($n=1$), and $C \le n^2 \approx 2.22$ in optical grade acrylic ($n=1.49$).
- **Solar Path Constraint**: Terrestrial solar trajectories span solar elevation angles between $\theta_{\text{elev}} \approx 15^\circ$ and $85^\circ$ depending on latitude and season. Restricting acceptance to this operational band enables $C_g > 1.5$.
- **Skew Ray Rejection**: Revolved 3D profiles do not conserve all edge rays due to angular momentum conservation. Anticipated optical rejection for off-axis skew rays ranges from 8% to 15%.

## 4. Performance Targets

| Metric | Target Baseline | Minimum Viable | Reference Note |
| :--- | :--- | :--- | :--- |
| Azimuthal Acceptance ($\Delta\phi$) | $360^\circ$ continuous | $180^\circ$ continuous | [[12-Omnidirectional-Concentration-Limits]] |
| Elevation Acceptance ($\Delta\theta$) | $20^\circ \text{ to } 75^\circ$ | $30^\circ \text{ to } 65^\circ$ | [[12-Omnidirectional-Concentration-Limits]] |
| Geometric Concentration ($C_g$) | $\ge 2.0\times$ | $\ge 1.5\times$ | [[32-Optical-Efficiency-Metrics]] |
| Optical Efficiency ($\eta_{\text{opt}}$) | $\ge 75\%$ in acceptance band | $\ge 65\%$ | [[32-Optical-Efficiency-Metrics]] |
| Mechanical Tracking | $0$ axes (fully static) | $1$ seasonal tilt shift/year | [[02-Research-Roadmap]] |

## 5. Scope Boundaries

- **In Scope**:
  - Non-imaging profile synthesis (CPC, DTIRC, toroidal reflectors).
  - Skew ray ray-tracing modeling in Python / open-source engines.
  - Optical material selection and transmission modeling (PMMA, glass).
  - Parametric design of receiver geometry (cylindrical, conical, flat disk).
- **Out of Scope**:
  - Grid-scale electrical inverter design.
  - Large-scale structural civil engineering foundations.
  - High-concentration imaging optics (parabolic dishes requiring mrad tracking accuracy).
