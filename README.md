# RoSoCol: Rotational Omnidirectional Solar Collector

Research repository and Obsidian vault for non-imaging optical systems focused on rotational omnidirectional solar concentration.

## Executive Summary

RoSoCol investigates static and semi-static non-imaging optical collectors that eliminate or minimize active dual-axis tracking. By leveraging rotational symmetry, these collectors achieve azimuthal invariance ($\Delta\phi = 360^\circ$) and optimize elevation acceptance ($\theta \in [\theta_{\min}, \theta_{\max}]$) within the thermodynamic limits of concentration.

## Fundamental Physical Constraints

Concentration in non-imaging optics is bounded by conservation of étendue (phase-space volume):

$$C_{3D, \max} = \frac{n_{\text{receiver}}^2 \sin^2\theta_{\text{out}}}{n_{\text{source}}^2 \sin^2\theta_{\text{in}}}$$

1. In air ($n_{\text{source}} = n_{\text{receiver}} = 1$) under hemispherical acceptance ($\theta_{\text{in}} = 90^\circ$, $\sin\theta_{\text{in}} = 1$), the maximum theoretical concentration is $C \le 1$.
2. In dielectric media ($n \approx 1.49$ for PMMA), the upper bound increases to $C \le n^2 \approx 2.22$.
3. To achieve meaningful geometric concentration ($C_g > 1.5$) without tracking, the system constrains elevation acceptance to the sun's seasonal path ($\theta_{\text{in}} \approx 23.5^\circ \text{ to } 60^\circ$) while maintaining continuous $360^\circ$ azimuthal reception.

## Repository and Vault Structure

The repository is structured as an Obsidian vault. All notes are formatted in standard Markdown with YAML frontmatter, LaTeX math blocks, and cross-references.

```
RoSoCol/
├── .obsidian/                       # Obsidian configuration
├── 00-Meta/                         # Vault indices, charter, roadmap
│   ├── 00-RoSoCol-Index.md          # Primary Map of Content (MOC)
│   ├── 01-Project-Scope-and-Charter.md
│   └── 02-Research-Roadmap.md
├── 01-Theory/                       # Non-imaging optics and thermodynamic limits
│   ├── 10-Non-Imaging-Optics-Foundations.md
│   ├── 11-Rotational-Symmetry-and-Phase-Space.md
│   └── 12-Omnidirectional-Concentration-Limits.md
├── 02-Geometries/                   # Profile geometries and concentrator classes
│   ├── 20-CPC-Solid-of-Revolution.md
│   ├── 21-Dielectric-TIR-Concentrators.md
│   └── 22-Toroidal-and-Annular-Architectures.md
├── 03-Modeling/                     # Ray tracing and mathematical formulation
│   ├── 30-Monte-Carlo-Ray-Tracing-Spec.md
│   ├── 31-Skew-Ray-Vector-Formulation.md
│   └── 32-Optical-Efficiency-Metrics.md
├── 04-Materials-and-Hardware/       # Substrates, coatings, receivers
│   ├── 40-Dielectrics-and-Transmission.md
│   ├── 41-Reflective-Surfaces-and-Coatings.md
│   └── 42-Receiver-and-Thermal-Coupling.md
├── 05-Literature/                   # Annotated bibliography and prior art
│   ├── 50-Foundational-Bibliography.md
│   └── 51-Prior-Art-and-Patents.md
├── assets/                          # Diagrams, ray plots, schematics
└── tools/                           # Analytical tools and profile generators
    └── cpc_profile_generator.py     # Parametric 2D/3D profile coordinate generator
```

## Getting Started

1. **Obsidian**: Open this directory directly in Obsidian via `Open folder as vault`.
2. **Navigation**: Start at [00-RoSoCol-Index.md](00-Meta/00-RoSoCol-Index.md) for the central Map of Content.
3. **Analytical Tools**: Run `python3 tools/cpc_profile_generator.py --help` to generate parametric surface profiles.
