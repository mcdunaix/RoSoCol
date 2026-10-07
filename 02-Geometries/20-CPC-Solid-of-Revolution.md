---
title: Compound Parabolic Concentrator Solid of Revolution
tags: [geometries, cpc, solid-of-revolution, truncation]
created: 2026-10-06
status: active
---

# Compound Parabolic Concentrator (CPC) Solid of Revolution

## Executive Takeaway
> **One-Breath Core Principle**: A Compound Parabolic Concentrator (CPC) redirects every photon entering within acceptance half-angle $\theta_a$ onto the absorber using tilted parabolic reflectors that satisfy the Abbe sine condition.
> **Operational Impact**: Ideal concentration scales as $1/\sin^2\theta_a$; wide seasonal acceptance ($\pm 35^\circ \text{ to } 60^\circ$) caps unboosted hollow concentration at $3.0\times \text{ to } 1.3\times$, requiring truncation to eliminate excessive height and material cost.

---

## Tool & Component Snapshot
| Tool / Concept | What It Does | Primary Decision / When to Use | Trade-off / Penalty |
| :--- | :--- | :--- | :--- |
| **Height Truncation ($H_t / H = 0.5\text{–}0.6$)** | Cuts the steep upper parabolic walls where curves become nearly parallel. | **Mandatory for all physical builds.** Saves $\sim 40\text{–}50\%$ height and material. | Loses only $5\text{–}10\%$ aperture diameter ($10\text{–}20\%$ concentration). |
| **Dielectric Medium ($n \approx 1.49$)** | Fills the collector cavity with solid PMMA or silicone. | Use when wide acceptance ($\pm 45^\circ$) is required without dropping concentration below $3\times$. | Adds bulk material weight and bulk absorption losses ($1\text{–}3\%/\text{cm}$). |
| **Parametric Generator (`cpc_profile_generator.py`)** | Computes analytical $(y, z)$ points and exports 3D Wavefront `.obj` meshes. | Use when generating CAD profiles, CNC tooling curves, or ray-tracer geometry. | Requires discrete meshing steps; skew rays in 3D drop optical efficiency to $\sim 90\%$. |

---

## Interactive Visual Parameter Explorer

Dial the acceptance angle, height truncation ratio, and receiver dimensions to see real-time profile cross-sections, ray tracing, and aspect ratio penalties:

```html-embed
assets/interactive/cpc-explorer.html
```

> **Fallback / Direct Launch**: If plugins are disabled, open [cpc-explorer.html](file:///Users/ofafonua/Documents/RoSoCol/assets/interactive/cpc-explorer.html) in any browser.

---

## Business & Decision Translation

### 1. The Geometric Concentration Bound
$$C_{3D, \text{geom}} = \frac{1}{\sin^2\theta_a}$$

- **CEO Summary**: There is a strict thermodynamic ceiling on concentration without motorized sun tracking. The wider you open the collector to catch morning, evening, and winter sun, the less light intensity you deliver to the cell.
- **The Dial We Turn**: Acceptance half-angle $\theta_a$.
- **The Business Cost**: Opening coverage from $\pm 25^\circ$ ($C = 5.6\times$) to $\pm 45^\circ$ ($C = 2.0\times$) discards $64\%$ of peak concentration.
- **When You Want This**: Whenever passive, non-tracking static operation is required across seasonal solar paths.

---

### 2. The Truncation Sweet Spot
- **CEO Summary**: An untruncated CPC has enormous upper walls that are virtually vertical. Truncating the top $40\text{–}50\%$ cut in half the height and material volume while sacrificing almost zero optical collection.
- **The Dial We Turn**: Truncation ratio $H_t / H_{\max}$ (dial to $0.5\text{–}0.6$).
- **When You Want This**: Every practical fabrication build.

---

## Deep Technical Specification & Math

The classical Compound Parabolic Concentrator (CPC), developed by Roland Winston, is the canonical non-imaging concentrator. Revolving the 2D profile about its central axis yields the 3D CPC.

### 1. 2D CPC Mathematical Formulation

Let:
- $a'$: Absorber half-width (or radius in 3D)
- $a$: Entrance aperture half-width (or radius in 3D)
- $\theta_a$: Design acceptance half-angle

From the edge-ray condition:
$$a = \frac{a'}{\sin\theta_a}$$
$$C_{2D} = \frac{a}{a'} = \frac{1}{\sin\theta_a}$$
$$C_{3D, \text{geom}} = \frac{\pi a^2}{\pi a'^2} = \left(\frac{a}{a'}\right)^2 = \frac{1}{\sin^2\theta_a}$$

#### Parametric Equations of the Profile
In polar coordinates $(\rho, \psi)$ measured from the focal point at the receiver edge:

$$\rho(\psi) = \frac{2 f'}{1 - \cos\psi} = \frac{2 a' (1 + \sin\theta_a)}{1 - \cos\psi}$$

For $\psi \in [2\theta_a, \theta_a + \pi/2]$.

In Cartesian coordinates $(y, z)$ where $z$ is the optical axis and $y$ is the transverse coordinate:

$$\left(y \cos\theta_a + z \sin\theta_a\right)^2 + 2 a' (1 + \sin\theta_a)^2 y - 2 a' (1 + \sin\theta_a) \cos\theta_a z - a'^2 (1 + \sin\theta_a)(3 + \sin\theta_a) = 0$$

#### Full CPC Total Height
The total vertical length $L$ of an untruncated CPC is:

$$L = \frac{a + a'}{\tan\theta_a} = \frac{a' (1 + \sin\theta_a)}{\tan\theta_a \sin\theta_a} = \frac{a' (1 + \sin\theta_a) \cos\theta_a}{\sin^2\theta_a}$$

As $\theta_a \to 0$, $L$ scales as $1/\sin^2\theta_a$. For wide-angle acceptance ($\theta_a \ge 30^\circ$), the profile remains compact.

### 2. Profile Truncation

The upper portion of a CPC parabola becomes nearly parallel to the optical axis ($dy/dz \approx 0$). It contributes very little additional aperture area while dramatically increasing reflector surface area, material volume, and height.

#### Truncation Trade-offs
- Truncating height by $50\%$ typically reduces aperture radius by only $5\text{--}10\%$.
- Concentration drops by $10\text{--}20\%$, but material and aspect ratio ($H/D$) improve by $50\%$.
- A truncated CPC operates closer to the practical optimum for stationary solar collectors.

### 3. Solid of Revolution: 3D Skew Ray Behavior

Revolving the 2D CPC profile about the $z$-axis creates a 3D concentrator. However:

- The 2D CPC is an **ideal concentrator** for meridional rays (all rays within $\pm\theta_a$ reach the absorber).
- The 3D revolved CPC is **not strictly ideal** because of **skew rays** (rays that do not pass through the optical axis).
- Skew rays can undergo multiple reflections and turn back out through the entrance aperture even when incident at angles $\theta < \theta_a$.
- Optical transmission for a 3D hollow CPC within the acceptance cone typically peaks at $\sim 90\text{--}96\%$, rather than $100\%$.
- The effective 3D concentration ratio achieved is:
  $$C_{3D, \text{eff}} = \eta_{\text{opt}} \cdot C_{3D, \text{geom}} \approx 0.90 \cdot \frac{1}{\sin^2\theta_a}$$

### 4. Implementation Reference

The profile generator script [cpc_profile_generator.py](file:///Users/ofafonua/Documents/RoSoCol/tools/cpc_profile_generator.py) implements the parametric equations above and supports:
- Full vs. truncated profile calculation
- Dielectric-filled CPC ($n > 1$) with corrected acceptance angles
- Exporting $(y, z)$ coordinates to CSV
- Generating 3D revolved `.obj` meshes for optical and mechanical CAD integration
