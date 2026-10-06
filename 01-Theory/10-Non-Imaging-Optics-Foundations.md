---
title: Non-Imaging Optics Foundations
tags: [theory, optics, etendue, thermodynamics]
created: 2026-10-06
status: active
---

# Non-Imaging Optics Foundations

Non-imaging optics (NIO) optimizes the transfer of radiant flux from a source to an absorber without preserving phase or point-to-point image fidelity. This section establishes the fundamental physical principles governing the RoSoCol system.

## 1. Conservation of Étendue

In Hamiltonian optics, a light ray in a three-dimensional medium is defined by its spatial coordinates $(x, y, z)$ and its optical direction cosines $(p_x, p_y, p_z)$, where $p_i = n k_i$ and $\sum k_i^2 = 1$.

The differential phase-space volume (geometric optical extent or étendue $\mathcal{E}$) is invariant along the optical path in lossless media (Liouville's theorem):

$$d\mathcal{E} = n^2 \, dx \, dy \, dp_x \, dp_y$$

Integrated over a spatial aperture area $A$ and a cone of rays with maximum semi-angle $\theta$ in a medium of refractive index $n$:

$$\mathcal{E} = \pi \, n^2 \, A \, \sin^2\theta$$

For any optical concentrator transferring radiant energy from an input aperture ($A_{\text{in}}$) to a receiver ($A_{\text{out}}$):

$$\mathcal{E}_{\text{out}} \ge \mathcal{E}_{\text{in}}$$

Equality ($\mathcal{E}_{\text{out}} = \mathcal{E}_{\text{in}}$) represents an ideal optical concentrator with zero phase-space dilution.

## 2. Thermodynamic Limit of Concentration

From the second law of thermodynamics, an absorber placed in an optical cavity cannot reach a temperature higher than the source. For a source subtending a half-angle $\theta_{\text{in}}$ entering a medium of refractive index $n_{\text{in}}$, exiting into a medium of refractive index $n_{\text{out}}$ over a half-angle $\theta_{\text{out}}$:

### Two-Dimensional (Trough) Geometry
$$C_{2D, \max} = \frac{A_{\text{in}}}{A_{\text{out}}} = \frac{n_{\text{out}} \sin\theta_{\text{out}}}{n_{\text{in}} \sin\theta_{\text{in}}}$$

Because the maximum physical collection angle at the absorber is $\theta_{\text{out}} = 90^\circ$ ($\sin\theta_{\text{out}} = 1$):

$$C_{2D, \max} = \frac{n_{\text{out}}}{n_{\text{in}} \sin\theta_{\text{in}}}$$

### Three-Dimensional (Axisymmetric / Revolved) Geometry
$$C_{3D, \max} = \frac{A_{\text{in}}}{A_{\text{out}}} = \frac{n_{\text{out}}^2 \sin^2\theta_{\text{out}}}{n_{\text{in}}^2 \sin^2\theta_{\text{in}}}$$

Setting $\theta_{\text{out}} = 90^\circ$:

$$C_{3D, \max} = \frac{n_{\text{out}}^2}{n_{\text{in}}^2 \sin^2\theta_{\text{in}}}$$

## 3. The Edge-Ray Principle

Imaging systems (e.g., parabolic dishes, Fresnel lenses) focus rays originating from a single point to another point. Due to geometric aberrations (spherical, coma, astigmatism), imaging concentrators achieve only a fraction (typically $25\% \text{ to } 50\%$) of the thermodynamic limit.

The **Edge-Ray Principle** (formulated by Roland Winston and Walter Welford) states:
> If an optical system redirects all rays originating from the boundary of the phase-space source to the boundary of the receiver phase space, then all rays originating from within the interior of the source phase space are guaranteed to reach the receiver.

Non-imaging profiles (such as the Compound Parabolic Concentrator) are generated directly by applying this boundary condition to reflector and refractor geometry.

## 4. Key Takeaways for RoSoCol

1. **Trade-Off**: Concentration ratio $C$ and acceptance half-angle $\theta_{\text{in}}$ are strictly reciprocal. Increasing angular acceptance directly decreases maximum achievable concentration.
2. **Dielectric Boost**: Immersing the receiver in a solid dielectric medium ($n > 1$) increases concentration by a factor of $n^2$ without decreasing angular acceptance.
3. **Phase Space Uniformity**: Any system design must minimize phase space dilution (rays passing through aperture but missing absorber, or exiting through entry aperture).
