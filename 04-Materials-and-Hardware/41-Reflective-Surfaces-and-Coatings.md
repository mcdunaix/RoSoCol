---
title: Reflective Surfaces and Coatings
tags: [materials, mirrors, coatings, reflectance]
created: 2026-10-06
status: active
---

# Reflective Surfaces and Coatings for Non-Imaging Optics

Hollow non-imaging concentrators rely on multiple internal specular reflections to channel edge rays to the receiver. The sensitivity of overall collector efficiency to surface reflectance is non-linear due to multiple reflections.

## 1. Multiple Reflections and Effective Reflectance

In imaging optics (e.g., parabolic trough or dish), nearly all rays undergo exactly one reflection ($m = 1$). In non-imaging concentrators, rays bounce multiple times.

The effective optical reflectance $\bar{\rho}_{\text{eff}}$ is governed by the mean number of reflections $\langle m \rangle$:

$$\bar{\rho}_{\text{eff}} = \rho^{\langle m \rangle}$$

For a 3D CPC with acceptance angle $\theta_a$:
- On-axis rays ($\theta \approx 0^\circ$): $m = 0 \text{ to } 1$.
- Extreme rays near the cutoff ($\theta \approx \theta_a$): $m = 2 \text{ to } 4$.
- Mean reflections across the acceptance cone: $\langle m \rangle \approx 1.3 \text{ to } 2.2$.

### Sensitivity Comparison

| Reflector Material | Specular Reflectance ($\rho$) | $m = 1$ Throughput | $m = 2$ Throughput | $m = 3$ Throughput |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Anodized Aluminum** | $0.85$ | $85.0\%$ | $72.3\%$ | $61.4\%$ |
| **Enhanced PVD Aluminum** | $0.90$ | $90.0\%$ | $81.0\%$ | $72.9\%$ |
| **Solar Silver Film (Alanod Miro-Sun)** | $0.95$ | $95.0\%$ | $90.3\%$ | $85.7\%$ |
| **Ultra-High Specular Silver (3M SMF-1100)**| $0.97$ | $97.0\%$ | $94.1\%$ | $91.3\%$ |

A shift from standard aluminum ($\rho = 0.85$) to solar silver ($\rho = 0.95$) increases total collector efficiency by over $25\%$ for double-bounce trajectories.

## 2. Coating Architectures

### Enhanced Aluminum (PVD Stack)
- **Substrate**: High-purity polished aluminum sheet (AA 1085).
- **Stack**: $\text{Al Substrate} \to \text{PVD Aluminum Layer} \to \text{Low-index } \text{SiO}_2 \to \text{High-index } \text{TiO}_2$.
- **Advantages**: Stable, resistant to moisture, lower cost.
- **Limitation**: Inter-band absorption dip near $\lambda = 800 \text{ nm}$ reduces integrated solar reflectance to $\le 90\%$.

### Protected Silver Film
- **Stack**: $\text{Polymer Carrier (PMMA/PET)} \to \text{PVD Pure Silver (Ag)} \to \text{Passivation Layer} \to \text{Adhesive}$.
- **Advantages**: Flat spectral reflectance ($\rho \ge 95\%$) across the entire solar spectrum ($350 - 2500 \text{ nm}$).
- **Vulnerabilities**: Silver tarnishes in the presence of atmospheric sulfur compounds ($\text{H}_2\text{S}$) and moisture if the edge seals fail.

## 3. Specular Error and Scattering

Surface slope errors $\sigma_{\text{slope}}$ and micro-roughness $\sigma_{\text{roughness}}$ scatter specular rays into non-specular diffuse cones:

$$R_{\text{spec}}(\theta) = R_{\text{total}} \cdot \exp\left[ -\left(\frac{4\pi \sigma_{\text{roughness}} \cos\theta}{\lambda}\right)^2 \right]$$

- For non-imaging concentrators with wide acceptance angles ($\theta_a \ge 20^\circ$), slope error tolerances are relatively generous: $\sigma_{\text{slope}} \le 5 \text{ mrad}$ (compared to $< 1 \text{ mrad}$ for imaging parabolic dishes).
- Standard commercially roll-formed reflective sheets meet this requirement without precision optical grinding.
