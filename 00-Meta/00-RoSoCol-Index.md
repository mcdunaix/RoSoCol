---
title: RoSoCol Map of Content (MOC)
tags: [moc, meta, index]
created: 2026-10-06
status: active
---

# RoSoCol Master Index

Central Map of Content for the Rotational Omnidirectional Solar Collector research project.

## 1. Project Management & Scope
- [[01-Project-Scope-and-Charter|Project Scope & Charter]]: Objectives, baseline performance targets, operational envelope.
- [[02-Research-Roadmap|Research Roadmap]]: Phase 1 to Phase 4 development plan, milestone gates, simulation deliverables.

## 2. Theoretical Foundations
- [[10-Non-Imaging-Optics-Foundations|Non-Imaging Optics Foundations]]: Étendue conservation, phase space, edge-ray principle, thermodynamic concentration limit.
- [[11-Rotational-Symmetry-and-Phase-Space|Rotational Symmetry & Phase Space]]: Clairaut's skew invariant, 2D to 3D profile revolution, skew-ray rejection mechanisms.
- [[12-Omnidirectional-Concentration-Limits|Omnidirectional Concentration Limits]]: Hemispherical bounds, dielectric $n^2$ enhancement, elevation-azimuth angular trade-offs.

## 3. Optical Architectures & Profiles
- [[20-CPC-Solid-of-Revolution|CPC Solid of Revolution]]: Classical Winston 3D CPC, truncation trade-offs, skew ray losses.
- [[21-Dielectric-TIR-Concentrators|Dielectric TIR Concentrators (DTIRC)]]: Solid refractive bodies, total internal reflection criteria, entry curvature.
- [[22-Toroidal-and-Annular-Architectures|Toroidal & Annular Architectures]]: Azimuthally continuous profiles, toroidal reflectors, annular receivers.

## 4. Computational Modeling & Ray Tracing
- [[30-Monte-Carlo-Ray-Tracing-Spec|Monte Carlo Ray Tracing Spec]]: Ray injection, source spectrum (ASTM G173-03), statistical convergence, divergence angles.
- [[31-Skew-Ray-Vector-Formulation|Skew Ray Vector Formulation]]: Vector Snell's law, 3D reflection operators, surface normals for quadric and revolved surfaces.
- [[32-Optical-Efficiency-Metrics|Optical Efficiency Metrics]]: Geometric concentration ratio, optical intercept factor, angular acceptance functions.

## 5. Materials, Coatings & Engineering
- [[40-Dielectrics-and-Transmission|Dielectrics & Transmission]]: PMMA, Borosilicate, Polycarbonate, spectral transmittance, UV degradation.
- [[41-Reflective-Surfaces-and-Coatings|Reflective Surfaces & Coatings]]: Specular reflectance, enhanced aluminum vs silver, incidence angle dependence.
- [[42-Receiver-and-Thermal-Coupling|Receiver & Thermal Coupling]]: PV cell types (monocrystalline Si, III-V multijunction), thermal flux management, passive heatsinking.

## 6. Literature & Prior Art
- [[50-Foundational-Bibliography|Foundational Bibliography]]: Winston, Welford, Rabl, Miñano, Benítez key references.
- [[51-Prior-Art-and-Patents|Prior Art & Patents]]: Analysis of static and rotational solar collectors, patent landscape, claims whitespace.

## 7. Computational Tools
- `tools/cpc_profile_generator.py`: Parametric generation of 2D/3D coordinates for non-imaging concentrators.
