---
title: Compound Parabolic Concentrator Solid of Revolution
tags: [geometries, cpc, solid-of-revolution, truncation]
created: 2026-10-06
status: active
---

# Compound Parabolic Concentrator (CPC) Solid of Revolution

The classical Compound Parabolic Concentrator (CPC), developed by Roland Winston, is the canonical non-imaging concentrator. Revolving the 2D profile about its central axis yields the 3D CPC.

## 1. 2D CPC Mathematical Formulation

Let:
- $a'$: Absorber half-width (or radius in 3D)
- $a$: Entrance aperture half-width (or radius in 3D)
- $\theta_a$: Design acceptance half-angle

From the edge-ray condition:
$$a = \frac{a'}{\sin\theta_a}$$
$$C_{2D} = \frac{a}{a'} = \frac{1}{\sin\theta_a}$$
$$C_{3D, \text{geom}} = \frac{\pi a^2}{\pi a'^2} = \left(\frac{a}{a'}\right)^2 = \frac{1}{\sin^2\theta_a}$$

### Parametric Equations of the Profile
In polar coordinates $(\rho, \psi)$ measured from the focal point at the receiver edge:

$$\rho(\psi) = \frac{2 f'}{1 - \cos\psi} = \frac{2 a' (1 + \sin\theta_a)}{1 - \cos\psi}$$

For $\psi \in [2\theta_a, \theta_a + \pi/2]$.

In Cartesian coordinates $(y, z)$ where $z$ is the optical axis and $y$ is the transverse coordinate:

$$\left(y \cos\theta_a + z \sin\theta_a\right)^2 + 2 a' (1 + \sin\theta_a)^2 y - 2 a' (1 + \sin\theta_a) \cos\theta_a z - a'^2 (1 + \sin\theta_a)(3 + \sin\theta_a) = 0$$

### Full CPC Total Height
The total vertical length $L$ of an untruncated CPC is:

$$L = \frac{a + a'}{\tan\theta_a} = \frac{a' (1 + \sin\theta_a)}{\tan\theta_a \sin\theta_a} = \frac{a' (1 + \sin\theta_a) \cos\theta_a}{\sin^2\theta_a}$$

As $\theta_a \to 0$, $L$ scales as $1/\sin^2\theta_a$. For wide-angle acceptance ($\theta_a \ge 30^\circ$), the profile remains compact.

## 2. Profile Truncation

The upper portion of a CPC parabola becomes nearly parallel to the optical axis ($dy/dz \approx 0$). It contributes very little additional aperture area while dramatically increasing reflector surface area, material volume, and height.

Truncation reduces the profile height from $L$ to $L_t < L$:
- Truncating $50\%$ of the height ($L_t = 0.5 L$) reduces the aperture radius $a_t$ by only $\sim 10\%$.
- The geometric concentration drops by $\sim 15\% \text{ to } 20\%$, but material cost and wind load drop by over $50\%$.
- Truncation increases the average angular acceptance for rays beyond the cutoff angle $\theta_a$, producing a smoother acceptance cutoff curve.

## 3. 3D Revolved CPC Dynamics

Revolving the 2D curve $(y(z), z)$ around $z=0$ defines a surface of revolution:

$$S(x, y, z) = x^2 + y^2 - [R(z)]^2 = 0$$

Where $R(z)$ is the radial distance computed from the 2D CPC parabola.

### Skew Ray Transmission Characteristics
- **Meridian Rays ($h = 0$)**: 100% transmission within $|\theta| \le \theta_a$ (assuming ideal specular reflectance).
- **Skew Rays ($h > 0$)**: Total internal transmission drops near the cutoff angle.
- **Integrated Optical Efficiency**:
  $$\bar{\eta}_{\text{opt}} = \frac{1}{\pi a^2 \sin^2\theta_a} \int_0^{\theta_a} \int_0^{2\pi} \tau(\theta, \phi) \sin\theta \cos\theta \, d\phi \, d\theta \approx 0.89 \text{ to } 0.91$$
- A 3D CPC collects roughly $90\%$ of the theoretical maximum 3D phase space.

## 4. Relevance to RoSoCol

A hollow 3D CPC provides an optical baseline for comparison. Its primary weakness in static omnidirectional solar collection is that if $\theta_a$ is set wide enough to cover seasonal variations ($\theta_a \approx 60^\circ$), $C_{3D} = 1/\sin^2(60^\circ) = 1.33\times$, which is insufficient to justify reflector manufacturing costs without dielectric enhancement or tailoring.
