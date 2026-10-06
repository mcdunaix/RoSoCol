---
title: Skew Ray Vector Formulation
tags: [modeling, skew-rays, vector-optics, clairaut]
created: 2026-10-06
status: active
---

# Skew Ray Vector Formulation and Invariant Proof

This note details the exact 3D vector mechanics for tracing skew rays on surfaces of revolution and proves the strict conservation of the skew invariant under specular reflection.

## 1. Surface of Revolution Geometry

A rotationally symmetric optical surface aligned with the $z$-axis is defined implicitly by:

$$F(x, y, z) = x^2 + y^2 - [R(z)]^2 = 0$$

Where $R(z)$ is the radial profile function and $R'(z) = \frac{dR}{dz}$.

The gradient vector of the surface is:

$$\nabla F = \begin{bmatrix} 2x \\ 2y \\ -2 R(z) R'(z) \end{bmatrix}$$

Normalizing yields the outward unit surface normal $\hat{\mathbf{n}}$ at intersection point $\mathbf{P} = (x, y, z)$:

$$\hat{\mathbf{n}}(x, y, z) = \frac{1}{\sqrt{x^2 + y^2 + [R(z) R'(z)]^2}} \begin{bmatrix} x \\ y \\ -R(z) R'(z) \end{bmatrix}$$

Note that the projection of $\hat{\mathbf{n}}$ onto the $xy$-plane points strictly in the radial direction $\hat{\mathbf{r}} = \frac{1}{r}(x \hat{\mathbf{x}} + y \hat{\mathbf{y}})$.

## 2. Ray Propagation and Intersection

A ray is parameterized by origin $\mathbf{P}_0 = (x_0, y_0, z_0)$ and unit direction vector $\mathbf{u} = (u_x, u_y, u_z)$:

$$\mathbf{P}(t) = \mathbf{P}_0 + t \mathbf{u}, \quad t > 0$$

Substituting into the surface equation yields the scalar root problem:

$$[x_0 + t u_x]^2 + [y_0 + t u_y]^2 - [R(z_0 + t u_z)]^2 = 0$$

- For conic profiles (paraboloid, ellipsoid, hyperboloid), $R^2(z)$ is quadratic in $z$, reducing the intersection equation to a closed-form quadratic polynomial $A t^2 + B t + C = 0$.
- For arbitrary non-imaging numerical profiles, root finding is solved using Newton-Raphson iteration with initial step estimate from bounding cylinders.

## 3. Strict Mathematical Proof of Skew Invariant Conservation

The skew invariant $h$ is the $z$-component of the ray's angular momentum vector $\mathbf{L} = \mathbf{P} \times \mathbf{u}$:

$$h = (\mathbf{P} \times \mathbf{u}) \cdot \hat{\mathbf{z}} = x u_y - y u_x$$

### Reflection Operator
Specular reflection reverses the normal component of ray velocity:

$$\mathbf{u}' = \mathbf{u} - 2 (\mathbf{u} \cdot \hat{\mathbf{n}}) \hat{\mathbf{n}}$$

### Invariant Transformation
The angular momentum after reflection is:

$$\mathbf{L}' = \mathbf{P} \times \mathbf{u}' = \mathbf{P} \times \left( \mathbf{u} - 2 (\mathbf{u} \cdot \hat{\mathbf{n}}) \hat{\mathbf{n}} \right) = (\mathbf{P} \times \mathbf{u}) - 2 (\mathbf{u} \cdot \hat{\mathbf{n}}) (\mathbf{P} \times \hat{\mathbf{n}})$$

Taking the dot product with $\hat{\mathbf{z}}$:

$$h' = h - 2 (\mathbf{u} \cdot \hat{\mathbf{n}}) [(\mathbf{P} \times \hat{\mathbf{n}}) \cdot \hat{\mathbf{z}}]$$

Examine the cross-product term $(\mathbf{P} \times \hat{\mathbf{n}}) \cdot \hat{\mathbf{z}}$:

$$(\mathbf{P} \times \hat{\mathbf{n}}) \cdot \hat{\mathbf{z}} = x n_y - y n_x$$

Substituting the normal vector components $n_x = C x$ and $n_y = C y$ (where $C = 1/\sqrt{x^2 + y^2 + [R R']^2}$):

$$x (C y) - y (C x) = C (x y - y x) = 0$$

Therefore:

$$h' = h - 0 = h$$

**Q.E.D.** Under specular reflection from any rotationally symmetric surface, the skew invariant $h$ is strictly conserved for every ray.

## 4. Consequences for Concentrator Turning Points

Because $h = r u_\phi = \text{constant}$ along the entire ray path:
- As the ray travels deeper into the concentrator where $r \to r_{\text{receiver}} \ll R_{\text{aperture}}$, the azimuthal direction cosine must grow:
  $$u_\phi(z) = \frac{h}{r(z)}$$
- Since total direction cosine magnitude cannot exceed unity ($u_r^2 + u_\phi^2 + u_z^2 = 1$):
  $$u_r^2 + u_z^2 = 1 - \frac{h^2}{r^2(z)}$$
- If a skew ray possesses $|h| > r_{\text{receiver}}$, there exists a critical radius $r_{\text{turn}} = |h|$ at which $u_r^2 + u_z^2 = 0$.
- The ray cannot penetrate to radii $r < r_{\text{turn}}$. It reflects off the caustic surface and reverses axial direction ($u_z \to -u_z$), escaping out of the entrance aperture.
- This proves analytically why 3D revolved CPCs inevitably suffer skew ray rejection near the receiver aperture.
