---
title: Research Roadmap
tags: [meta, roadmap, milestones]
created: 2026-10-06
status: active
---

# Research Roadmap: RoSoCol

Structured execution plan for the investigation, simulation, and hardware realization of the Rotational Omnidirectional Solar Collector.

## Phase 1: Theoretical Modeling and Physical Bounds
- [ ] Define analytical phase space representation for diurnal solar transit at latitudes $25^\circ \text{N}$ to $45^\circ \text{N}$.
- [ ] Calculate theoretical maximum concentration ratio $C_{\max}(\theta_{\min}, \theta_{\max})$ as a function of elevation acceptance.
- [ ] Formalize skew ray invariant equations for rotational quadrics and revolved non-imaging surfaces.
- **Deliverable**: Theoretical limits baseline document [[12-Omnidirectional-Concentration-Limits]].

## Phase 2: Geometric Synthesis and Profiling
- [ ] Develop parametric coordinate generator for 3D revolved CPC and truncated CPC profiles (`tools/cpc_profile_generator.py`).
- [ ] Synthesize solid dielectric TIR profile (DTIRC) with curved entry aperture to minimize front-surface Fresnel loss.
- [ ] Evaluate toroidal concentrator geometries paired with vertical cylindrical absorbers.
- **Deliverable**: Open-source analytical profile generator and CAD profile point clouds.

## Phase 3: Monte Carlo Ray Tracing Simulation
- [ ] Construct vectorized 3D Monte Carlo ray tracer implementing vector Snell's law and Fresnel reflection coefficients.
- [ ] Run ray tracing across incident grid: $\theta \in [0^\circ, 90^\circ]$ in $1^\circ$ steps, $\phi \in [0^\circ, 360^\circ]$ in $15^\circ$ steps ($N = 10^5 \text{ rays/step}$).
- [ ] Compute flux distribution across receiver surface to identify hot spots and non-uniformity ratios.
- [ ] Quantify skew-ray leakage as a function of concentrator aspect ratio ($H / R$).
- **Deliverable**: Optical transmission curves and flux distribution maps.

## Phase 4: Materials, Thermal Management, and Prototyping
- [ ] Evaluate optical grade PMMA vs BK7/borosilicate glass for transmission, mass, and UV stability.
- [ ] Model passive thermal heat rejection on concentrated receiver under $C_g = 2.5\times$ (approx. $2.5 \text{ kW/m}^2$ peak solar flux).
- [ ] CNC mill or 3D optical print (stereolithography with post-cure polishing) a sub-scale collector prototype ($D = 150 \text{ mm}$).
- [ ] Indoor solar simulator test: Measure angular transmission profile using calibrated silicon photodiode.
- **Deliverable**: Prototype validation report and bench test characterization.
