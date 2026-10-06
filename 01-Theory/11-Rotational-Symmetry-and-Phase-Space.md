---
title: Rotational Symmetry and Phase Space
tags: [theory, rotational-symmetry, skew-rays, clairaut]
created: 2026-10-06
status: active
---

# Rotational Symmetry and Phase Space in 3D Non-Imaging Optics

A rotational concentrator possesses rotational symmetry about a central axis (conventionally $\hat{z}$). While rotational symmetry simplifies manufacturing and provides continuous azimuthal acceptance ($\Delta\phi = 360^\circ$), it introduces fundamental phase-space limitations not present in 2D trough systems.

## 1. Meridian Rays vs. Skew Rays

Rays traversing a rotationally symmetric optical system fall into two distinct classes:

1. **Meridian Rays**: Rays that lie in a plane containing the axis of revolution ($\hat{z}$). Because the surface normal also lies in this meridian plane, the ray remains confined to the plane throughout all reflections and refractions.
2. **Skew Rays**: Rays that do not intersect the axis of revolution. Skew rays possess non-zero angular momentum about the symmetry axis.

## 2. Conservation of Skew Invariant (Clairaut's Relation)

In any optical system with rotational symmetry about the $z$-axis, the generalized momentum conjugate to the azimuthal angle $\phi$ is conserved. In Cartesian coordinates $(x, y, z)$ with direction cosines $(k_x, k_y, k_z)$ and refractive index $n$:

$$p_\phi = n \left( x k_y - y k_x \right) = \text{constant}$$

In cylindrical coordinates $(r, \phi, z)$, if $\alpha$ is the angle between the ray direction and the meridian plane, and $\beta$ is the angle between the projection of the ray on the meridian plane and the surface tangent:

$$h = n \, r \sin\alpha = \text{constant}$$

This constant $h$ is the **skew invariant** (analogous to angular momentum in classical mechanics).

## 3. Why Revolved 2D Profiles Fail to be Ideal in 3D

A common design approach revolves an ideal 2D non-imaging profile (such as a 2D Compound Parabolic Concentrator) about its central axis to create a 3D solid of revolution.

### The Skew Ray Rejection Problem
- **Meridian Ray Behavior**: Every meridian ray entering within the design acceptance half-angle $\theta_{\text{in}}$ satisfies the 2D edge-ray conditions and reaches the absorber.
- **Skew Ray Behavior**: Because $h = n r \sin\alpha$ is conserved, as a skew ray propagates toward the receiver (where the radius $r$ decreases from $R_{\text{in}}$ to $R_{\text{out}}$), the term $\sin\alpha$ must increase:
  $$\sin\alpha(z) = \frac{h}{n \, r(z)}$$
- If the ray has a sufficiently large initial $h$, a point is reached where $\sin\alpha$ would have to exceed $1.0$.
- Before this mathematical singularity can occur, the ray encounters a turning point (caustic) where it reverses its axial direction ($\dot{z}$ changes sign) and reflects back out through the entrance aperture.

### Quantitative Consequence
The ideal 3D thermodynamic concentration limit is:
$$C_{3D, \max} = \frac{1}{\sin^2\theta_{\text{in}}}$$

A revolved 3D CPC achieves:
$$C_{\text{geometric}} = \frac{R_{\text{in}}^2}{R_{\text{out}}^2} = \frac{1}{\sin^2\theta_{\text{in}}}$$

However, its **transmission efficiency** $\eta(\theta)$ drops off inside the acceptance angle due to skew ray rejection:
- For $0 \le \theta \le \theta_{\text{in}}$, average transmission is typically $\eta \approx 88\% \text{ to } 92\%$, rather than $100\%$.
- Approximately $8\% \text{ to } 12\%$ of the incident phase-space within the acceptance cone is rejected back out of the aperture.

## 4. Architectural Mitigation Strategies for RoSoCol

1. **Receiver Geometry Tailoring**: Replacing a flat circular receiver with a spherical, conical, or vertical cylindrical receiver reduces the minimum radius constraint, lowering $h_{\text{crit}}$ rejection.
2. **Dielectric Filling (DTIRC)**: A higher refractive index $n$ compresses the internal ray cone via Snell's law, drastically reducing the angle $\alpha$ and preventing turning points before the absorber.
3. **Truncation**: Truncating the upper third to half of the concentrator profile significantly reduces profile height and reflector absorption with negligible reduction in acceptance.
