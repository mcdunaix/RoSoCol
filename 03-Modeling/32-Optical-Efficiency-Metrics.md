---
title: Optical Efficiency Metrics
tags: [modeling, metrics, concentration-ratio, efficiency]
created: 2026-10-06
status: active
---

# Optical Efficiency and Performance Metrics

Standardized mathematical metrics used to evaluate and compare RoSoCol optical geometries.

## 1. Geometric Concentration Ratio ($C_g$)

The geometric ratio of total active entrance aperture area $A_{\text{entry}}$ to total receiver surface area $A_{\text{receiver}}$:

$$C_g = \frac{A_{\text{entry}}}{A_{\text{receiver}}}$$

- For a flat disk receiver in a circular 3D CPC: $C_g = \frac{\pi R_{\text{in}}^2}{\pi R_{\text{out}}^2} = \left(\frac{R_{\text{in}}}{R_{\text{out}}}\right)^2$.
- For an annular aperture focused on a vertical cylinder: $C_g = \frac{\pi (R_2^2 - R_1^2)}{2\pi r_{\text{abs}} H_{\text{abs}}}$.

## 2. Instantaneous Optical Efficiency ($\eta_{\text{opt}}$)

The fraction of radiant flux entering the physical aperture that is successfully absorbed by the receiver at incident solar position $(\theta_s, \phi_s)$:

$$\eta_{\text{opt}}(\theta_s, \phi_s) = \frac{\Phi_{\text{receiver}}(\theta_s, \phi_s)}{\Phi_{\text{aperture}}(\theta_s, \phi_s)}$$

Expressed in terms of loss mechanisms:

$$\eta_{\text{opt}}(\theta_s, \phi_s) = \gamma(\theta_s, \phi_s) \cdot \bar{\rho}^{\langle m \rangle} \cdot \tau_{\text{bulk}} \cdot (1 - R_{\text{Fresnel}})$$

Where:
- $\gamma(\theta_s, \phi_s)$: Optical intercept factor (fraction of rays reaching the absorber assuming lossless surfaces).
- $\bar{\rho}$: Average specular surface reflectance ($\approx 0.92 \text{ to } 0.95$ for silvered aluminum).
- $\langle m \rangle$: Mean number of reflections per accepted ray path.
- $\tau_{\text{bulk}}$: Internal bulk transmittance through dielectric media ($\exp(-\alpha L)$).
- $R_{\text{Fresnel}}$: Front surface reflection loss at dielectric entry interfaces.

## 3. Local Flux Concentration Ratio ($C_{\text{flux}}$)

Concentration is non-uniform across the receiver surface. The local flux concentration is the ratio of local irradiance $I(x, y)$ to incident aperture irradiance $I_0$:

$$C_{\text{flux}}(x, y) = \frac{I(x, y)}{I_0}$$

### Flux Uniformity Metrics
Non-uniform flux creates severe mismatch losses in photovoltaic cells and localized thermal stress.
- **Peak-to-Average Flux Ratio**:
  $$\xi_{\text{flux}} = \frac{\max_{(x,y)} C_{\text{flux}}(x, y)}{\bar{C}_{\text{flux}}}$$
  Design target for RoSoCol: $\xi_{\text{flux}} \le 2.5$ across operating angles.

## 4. Angular Acceptance Function ($\tau(\theta)$)

For a rotationally symmetric system, $\eta_{\text{opt}}$ is azimuthally invariant ($\eta_{\text{opt}}(\theta, \phi) = \tau(\theta)$).

- **Nominal Acceptance Angle ($\theta_a$)**: The design cutoff angle determined by the 2D profile.
- **Half-Power Acceptance Angle ($\theta_{50}$)**: The incidence angle at which optical transmission drops to $50\%$ of its on-axis peak:
  $$\tau(\theta_{50}) = 0.50 \cdot \tau(0^\circ)$$
- **Acceptance Sharpness Factor**:
  $$S_a = \left| \frac{d\tau}{d\theta} \right|_{\theta = \theta_a}$$
  Ideal 2D CPCs exhibit step-function cutoffs ($S_a \to \infty$). 3D CPCs exhibit continuous roll-off due to skew-ray leakage.

## 5. Annual Optical Yield ($Y_{\text{annual}}$)

The total radiant energy delivered to the receiver per unit aperture area over an annual meteorological year:

$$Y_{\text{annual}} = \int_{\text{year}} I_{\text{DNI}}(t) \cos\theta_s(t) \, \tau(\theta_s(t)) \, dt + \int_{\text{year}} I_{\text{diffuse}}(t) \, \bar{\tau}_{\text{diffuse}} \, dt$$

Where diffuse acceptance is the hemispherical integral:

$$\bar{\tau}_{\text{diffuse}} = \frac{1}{\pi} \int_0^{2\pi} d\phi \int_0^{\pi/2} \tau(\theta) \sin\theta \cos\theta \, d\theta = \frac{\tau(0)}{C_g}$$
