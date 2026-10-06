---
title: Omnidirectional Concentration Limits
tags: [theory, concentration-limits, omnidirectional, solar-geometry]
created: 2026-10-06
status: active
---

# Omnidirectional Concentration Limits

The term *omnidirectional* requires rigorous optical definition. In radiant energy transfer, collection over a full hemisphere ($2\pi$ steradians) imposes strict thermodynamic upper bounds on concentration.

## 1. The Hemispherical Thermodynamic Bound

Consider a stationary collector receiving light from all directions across the upper hemisphere ($\theta_{\text{in}} \in [0, \pi/2]$ and $\phi_{\text{in}} \in [0, 2\pi]$).

The projected solid angle subtended by the hemispherical source is:

$$\Omega_{\text{hemi}} = \int_0^{2\pi} d\phi \int_0^{\pi/2} \sin\theta \cos\theta \, d\theta = \pi \text{ sr}$$

At the receiver, the maximum possible projected solid angle into which light can be delivered is also $\pi \text{ sr}$ (if the receiver is in a medium of refractive index $n_r = 1$).

From the second law of thermodynamics:

$$C_{\text{hemi}, \max} = \frac{A_{\text{in}}}{A_{\text{out}}} \le \frac{n_r^2 \Omega_{\text{receiver}}}{n_s^2 \Omega_{\text{source}}} = \frac{n_r^2 \cdot \pi}{1^2 \cdot \pi} = n_r^2$$

### Physical Realities
- **Air-filled collector ($n_r = 1$)**: $C_{\max} \le 1.0$. True omnidirectional concentration in air is impossible. Any optical system with hemispherical acceptance in air produces $C \le 1$.
- **Solid dielectric collector ($n_r = 1.49$, PMMA)**: $C_{\max} \le (1.49)^2 \approx 2.22$. A solid acrylic concentrator accepting light from the entire hemisphere can concentrate flux by at most $2.22\times$.
- **High-index glass ($n_r = 1.80$)**: $C_{\max} \le (1.80)^2 \approx 3.24$.

## 2. Annular Phase-Space Tailoring (Solar-Specific Omnidirectionality)

The sun does not illuminate the entire hemisphere uniformly. Direct normal irradiance (DNI) follows a deterministic path across the sky dictated by solar elevation $\alpha_s$ and solar azimuth $\gamma_s$:

$$\sin\alpha_s = \sin\phi_L \sin\delta + \cos\phi_L \cos\delta \cos\omega$$

Where:
- $\phi_L$: Local latitude
- $\delta$: Solar declination ($-23.45^\circ \le \delta \le +23.45^\circ$)
- $\omega$: Hour angle ($15^\circ/\text{hour}$)

### Elevation Band Acceptance
A rotational collector can maintain complete azimuthal omnidirectionality ($\phi \in [0, 2\pi]$) while restricting polar angle acceptance to an annular band $\theta \in [\theta_1, \theta_2]$ (where $\theta$ is zenith angle, $\theta = 90^\circ - \alpha_s$).

The projected solid angle of this annular source is:

$$\Omega_{\text{annular}} = \int_0^{2\pi} d\phi \int_{\theta_1}^{\theta_2} \sin\theta \cos\theta \, d\theta = \pi \left( \sin^2\theta_2 - \sin^2\theta_1 \right)$$

The maximum theoretical concentration ratio for this annular band into an absorber immersed in medium $n_r$ with hemispherical emission ($\theta_{\text{out}} = 90^\circ$) is:

$$C_{\text{annular}, \max} = \frac{n_r^2 \pi}{\Omega_{\text{annular}}} = \frac{n_r^2}{\sin^2\theta_2 - \sin^2\theta_1}$$

### Worked Example: Mid-Latitude Installation ($\text{Latitude } 35^\circ \text{N}$)
For an un-tracked horizontal aperture at $35^\circ \text{N}$:
- Minimum summer solar zenith angle: $\theta_{\min} \approx 35^\circ - 23.45^\circ = 11.55^\circ$ ($\sin\theta_1 \approx 0.200$)
- Maximum winter solar zenith angle for effective collection ($\alpha_s \ge 15^\circ$): $\theta_{\max} \approx 75^\circ$ ($\sin\theta_2 \approx 0.966$)

Calculating theoretical maximum concentration:
$$\sin^2(75^\circ) - \sin^2(11.55^\circ) = (0.9659)^2 - (0.2002)^2 = 0.933 - 0.040 = 0.893$$

$$C_{\text{air}, \max} = \frac{1}{0.893} \approx 1.12\times$$
$$C_{\text{PMMA}, \max} = \frac{(1.49)^2}{0.893} = \frac{2.22}{0.893} \approx 2.49\times$$

If seasonal manual adjustment is permitted twice per year, the elevation band narrows to $\Delta\theta \approx 30^\circ$ ($\theta \in [20^\circ, 50^\circ]$):
$$\sin^2(50^\circ) - \sin^2(20^\circ) = 0.587 - 0.117 = 0.470$$

$$C_{\text{air}, \max} = \frac{1}{0.470} \approx 2.13\times$$
$$C_{\text{PMMA}, \max} = \frac{2.22}{0.470} \approx 4.72\times$$

## 3. Conclusions for RoSoCol Architecture

1. **Pure Static Air Optics**: A completely static air-filled collector covering full seasonal daylight yields negligible concentration ($C < 1.2\times$).
2. **Dielectric Requirement**: To achieve meaningful static concentration ($C_g \ge 2.0\times$), RoSoCol must either:
   - Use a solid dielectric body ($n \ge 1.49$), or
   - Implement an annular toroidal geometry focused on a vertical cylindrical receiver.
3. **Hybrid Seasonal Tilt**: A rotational design that allows a single seasonal tilt axis or latitude-tuned baseline geometry maximizes annual yield.
