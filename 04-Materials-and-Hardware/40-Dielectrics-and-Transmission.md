---
title: Dielectrics and Transmission Materials
tags: [materials, dielectrics, pmma, transmission, solar-spectrum]
created: 2026-10-06
status: active
---

# Optical Dielectrics and Transmission Materials

Selection and characterization of solid transparent media for Dielectric Totally Internally Reflecting Concentrators (DTIRC) and protective optical domes.

## 1. Candidate Material Matrix

| Material | Refractive Index ($n_d$, $589 \text{ nm}$) | Solar Transmittance ($\tau_{\text{solar}}$, $3 \text{ mm}$) | Max Service Temp ($^\circ\text{C}$) | Density ($\text{g/cm}^3$) | UV Degradation Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PMMA (Optical Grade)** | $1.491$ | $92.3\%$ | $85^\circ\text{C}$ | $1.19$ | Low (<0.5% loss / 10 yr) |
| **Borosilicate 33 (Glass)** | $1.472$ | $91.8\%$ | $450^\circ\text{C}$ | $2.23$ | Zero |
| **Polycarbonate (PC)** | $1.586$ | $88.5\%$ | $120^\circ\text{C}$ | $1.20$ | High without hardcoat |
| **Optical Silicone (PDMS)** | $1.410$ | $93.1\%$ | $180^\circ\text{C}$ | $1.03$ | Very low |

## 2. Spectral Dispersion and Sellmeier Formulation

The refractive index varies across the solar spectrum ($\lambda \in [0.35, 2.0] \, \mu\text{m}$). For optical PMMA, the three-term Sellmeier equation describes dispersion:

$$n^2(\lambda) - 1 = \frac{B_1 \lambda^2}{\lambda^2 - C_1} + \frac{B_2 \lambda^2}{\lambda^2 - C_2} + \frac{B_3 \lambda^2}{\lambda^2 - C_3}$$

For PMMA at $20^\circ\text{C}$:
- $B_1 = 1.1819, \quad C_1 = 0.00938 \, \mu\text{m}^2$
- $B_2 = 0.0475, \quad C_2 = 0.0274 \, \mu\text{m}^2$
- $B_3 = 0.9442, \quad C_3 = 100.0 \, \mu\text{m}^2$

### Chromatic Aberration Impact
Because non-imaging optics does not form point images, chromatic aberration does not defocus rays into blur circles. Instead, dispersion shifts the critical angle:
$$\Delta\theta_c = \theta_c(\lambda_1) - \theta_c(\lambda_2) = \arcsin\left(\frac{1}{n(\lambda_1)}\right) - \arcsin\left(\frac{1}{n(\lambda_2)}\right)$$
For PMMA between $400 \text{ nm}$ ($n \approx 1.505$) and $1000 \text{ nm}$ ($n \approx 1.485$):
$$\theta_c(400\text{ nm}) = 41.6^\circ, \quad \theta_c(1000\text{ nm}) = 42.3^\circ$$
A margin of $\ge 1.5^\circ$ above nominal $\theta_c$ prevents chromatic TIR leakage in the near-infrared spectrum.

## 3. Bulk Optical Absorption (Beer-Lambert Law)

Internal transmission over optical path length $L$ through a dielectric is:

$$\tau_{\text{bulk}}(\lambda) = \exp\left( -\alpha(\lambda) \cdot L \right)$$

Where $\alpha(\lambda)$ is the spectral absorption coefficient:
- In PMMA: $\alpha \le 0.005 \text{ cm}^{-1}$ between $400 \text{ nm}$ and $850 \text{ nm}$.
- Strong C-H vibrational absorption overtones emerge above $1150 \text{ nm}$ and $1400 \text{ nm}$.
- For ray paths $L \le 10 \text{ cm}$, total broadband solar transmission exceeds $90\%$.
- For large optics with $L > 25 \text{ cm}$, bulk absorption penalties exceed $15\%$, making solid dielectric concentrators unviable compared to hollow reflectors.

## 4. Engineering Recommendation for RoSoCol

1. **Sub-scale Prototypes ($D \le 200 \text{ mm}$)**: Cast optical PMMA (Plexiglas Solar grade). Injection molding or diamond CNC turning allows rapid prototyping of rotationally symmetric DTIRC profiles.
2. **Thermal Coupling**: Use optical elastomeric silicone (e.g. Dow Sylgard 184 or Shin-Etsu KER-2500) to bond the dielectric base directly to the PV receiver, eliminating Fresnel reflection at the exit aperture ($R_{\text{interface}} < 0.1\%$).
