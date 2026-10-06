---
title: Dielectric Total Internal Reflection Concentrators (DTIRC)
tags: [geometries, dtirc, total-internal-reflection, dielectrics]
created: 2026-10-06
status: active
---

# Dielectric Total Internal Reflection Concentrators (DTIRC)

A Dielectric Totally Internally Reflecting Concentrator (DTIRC) replaces hollow metallic reflective cavities with a solid optical dielectric body (such as PMMA or optical glass).

## 1. Operating Principle

A DTIRC relies on two optical mechanisms:
1. **Refraction at the Entrance Aperture**: External rays incident at angle $\theta_{\text{in}}$ are refracted by Snell's law into internal angles $\theta_{\text{int}} = \arcsin\left(\frac{\sin\theta_{\text{in}}}{n}\right)$. This compresses the internal angular spread.
2. **Total Internal Reflection (TIR) at Sidewalls**: Internal rays strike the dielectric-air boundary at angles $\theta > \theta_c = \arcsin(1/n)$. Under TIR, reflectance is strictly $100\%$ ($\rho = 1.000$), completely eliminating the metallic absorption losses of silver ($\rho \approx 0.95$) or aluminum ($\rho \approx 0.90$).

## 2. Geometric and Physical Limits

Because the receiver is optically coupled to the dielectric medium ($n_r = n$), the 3D concentration limit scales by $n^2$:

$$C_{3D, \text{DTIRC}, \max} = \frac{n^2}{\sin^2\theta_a}$$

For optical grade PMMA ($n = 1.491$ at $\lambda = 589 \text{ nm}$):
$$n^2 \approx 2.223$$

For an acceptance half-angle $\theta_a = 45^\circ$:
- Hollow 3D CPC in air: $C_{\text{geom}} = \frac{1}{\sin^2(45^\circ)} = 2.00\times$
- 3D DTIRC: $C_{\text{geom}} = \frac{(1.491)^2}{\sin^2(45^\circ)} \approx 4.45\times$

## 3. Surface Profile Construction

A classical DTIRC consists of three distinct geometric zones:
1. **Curved Front Entry Surface**: A convex spherical or aspherical cap that provides optical power, reducing ray divergence before internal reflections.
2. **TIR Sidewall Profile**: Shaped using the edge-ray method where the local tangent ensures all extreme rays satisfy $\theta_{\text{incident}} \ge \theta_c$.
3. **Optically Coupled Exit Aperture**: A planar base glued or bonded with optical silicone/index-matching gel to the receiver (PV cell).

### Sidewall Governing Differential Equation
For a polar profile $r(\theta)$ with receiver at the origin:

$$\frac{dr}{d\theta} = r \tan\left[ \frac{\theta - \arcsin\left(\frac{1}{n}\right) + \gamma}{2} \right]$$

Where $\gamma$ is the local angle between the extreme ray wavefront and the radial vector.

## 4. Trade-Offs for RoSoCol

| Parameter | Air-Filled Metallic CPC | Solid DTIRC |
| :--- | :--- | :--- |
| Max Concentration ($C_{\max}$) | $\frac{1}{\sin^2\theta_a}$ | $\frac{n^2}{\sin^2\theta_a}$ ($2.22\times$ higher) |
| Sidewall Reflection Loss | $5\% \text{ to } 12\%$ per bounce | $0.0\%$ (under pure TIR) |
| Front Surface Fresnel Loss | $0.0\%$ (open cavity) | $\sim 4.0\%$ per entry ($R = \left(\frac{n-1}{n+1}\right)^2$) |
| Volumetric Mass / Weight | Low (thin sheet metal) | High ($M \propto V \cdot \rho_{\text{PMMA}}$) |
| Manufacturing Method | Sheet hydroforming / stamping | Injection molding / casting |
| Thermal Sensitivity | Excellent ($T > 250^\circ\text{C}$) | Limited by PMMA glass transition ($T_g \approx 105^\circ\text{C}$) |

## 5. Architectural Recommendation for RoSoCol

For small to medium aperture diameters ($D_{\text{in}} \le 250 \text{ mm}$), DTIRC is the superior architecture for stationary concentration due to the $n^2$ multiplier and zero reflection degradation over multi-bounce paths. For larger scales ($D_{\text{in}} > 500 \text{ mm}$), excessive mass and internal bulk absorption favor hollow toroidal or segmented architectures.
