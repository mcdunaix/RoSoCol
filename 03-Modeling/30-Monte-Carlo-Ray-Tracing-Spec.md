---
title: Monte Carlo Ray Tracing Specification
tags: [modeling, mcrt, ray-tracing, simulation-spec]
created: 2026-10-06
status: active
---

# Monte Carlo Ray Tracing (MCRT) Specification

This document defines the simulation standards, source models, and statistical bounds required for numerical validation of RoSoCol optical geometries.

## 1. Solar Source Characterization

### Angular Subtense (Sunshape)
The solar disk subtends a finite angular diameter at the Earth's surface:
- **Mean Solar Angular Radius**: $\theta_{\text{sun}} = 4.65 \text{ mrad} \approx 0.2664^\circ$.
- **Standard Sunshape Models**:
  1. *Pillbox Model*: Uniform radiant intensity across $|\theta| \le \theta_{\text{sun}}$.
  2. *Buie Sunshape Model*: Empirically accounts for atmospheric circumsolar scattering:
     $$\phi(\theta) = \begin{cases} \frac{\cos(0.326\theta)}{\cos(0.305\theta)} & \text{for } 0 \le \theta \le \theta_{\text{sun}} \\ \exp(\kappa) \theta^\gamma & \text{for } \theta > \theta_{\text{sun}} \end{cases}$$
     Where circumsolar ratio (CSR) ranges from $0.02$ (clear sky) to $0.15$ (hazy sky).

### Spectral Weighting
For broadband photovoltaic modeling, rays are weighted according to the ASTM G173-03 AM1.5 Direct + Circumsolar spectrum ($\lambda \in [300, 2500] \text{ nm}$):

$$w_i = \frac{I_{\text{AM1.5}}(\lambda_i) \cdot \Delta\lambda}{\sum I_{\text{AM1.5}}(\lambda) \Delta\lambda}$$

## 2. Ray Generation and Injection Pipeline

1. **Spatial Sampling**:
   Rays are injected across the entrance aperture $A_{\text{in}}$. For a circular aperture of radius $R$:
   $$r = R \sqrt{\xi_1}, \quad \phi = 2\pi \xi_2$$
   Where $\xi_1, \xi_2 \sim \mathcal{U}(0, 1)$ are pseudo-random uniform variates. This preserves uniform spatial density ($dA = r \, dr \, d\phi$).

2. **Angular Sampling**:
   For a given solar pointing vector $\mathbf{S}_0 = (\sin\theta_s \cos\phi_s, \sin\theta_s \sin\phi_s, \cos\theta_s)$:
   Perturb ray direction by sampling from the sunshape cone:
   $$\theta_p = \theta_{\text{sun}} \sqrt{\xi_3}, \quad \phi_p = 2\pi \xi_4$$

## 3. Surface Interaction Operators

At each ray-surface intersection point $\mathbf{x}_{\text{int}}$ with surface unit normal $\hat{\mathbf{n}}$:

### Specular Reflection
$$\mathbf{k}_{\text{refl}} = \mathbf{k}_{\text{inc}} - 2 \left( \mathbf{k}_{\text{inc}} \cdot \hat{\mathbf{n}} \right) \hat{\mathbf{n}}$$
Ray energy is updated by the material specular reflectance:
$$E_{m+1} = E_m \cdot \rho(\theta_{\text{inc}}, \lambda)$$

### Dielectric Refraction (Snell's Law)
$$\mathbf{k}_{\text{refr}} = \frac{n_1}{n_2} \mathbf{k}_{\text{inc}} + \left[ \frac{n_1}{n_2} \cos\theta_1 - \sqrt{1 - \left(\frac{n_1}{n_2}\right)^2 (1 - \cos^2\theta_1)} \right] \hat{\mathbf{n}}$$
If $1 - \left(\frac{n_1}{n_2}\right)^2 (1 - \cos^2\theta_1) < 0$, total internal reflection (TIR) occurs ($\rho = 1.000$, $\mathbf{k} = \mathbf{k}_{\text{refl}}$).

### Fresnel Power Splitting
For unpolarized solar radiation, reflection probability at non-TIR interfaces:
$$R(\theta) = \frac{R_s + R_p}{2}$$
$$R_s = \left| \frac{n_1 \cos\theta_1 - n_2 \cos\theta_2}{n_1 \cos\theta_1 + n_2 \cos\theta_2} \right|^2, \quad R_p = \left| \frac{n_1 \cos\theta_2 - n_2 \cos\theta_1}{n_1 \cos\theta_2 + n_2 \cos\theta_1} \right|^2$$

## 4. Termination and Convergence Bounds

A ray trajectory is terminated if:
1. It strikes the designated receiver boundary ($E_{\text{abs}} = E_{\text{final}}$).
2. It reflects back out of the entrance aperture (rejected ray).
3. Total bounce count exceeds $N_{\max} = 50$.
4. Remaining ray energy drops below threshold: $E / E_0 < 10^{-4}$.

### Statistical Error Estimation
For $N$ rays launched, the estimated optical transmission $\hat{\eta} = N_{\text{absorbed}} / N$ has standard error:

$$\sigma_{\hat{\eta}} = \sqrt{\frac{\hat{\eta} (1 - \hat{\eta})}{N}}$$

To achieve uncertainty $\sigma_{\hat{\eta}} \le 0.001$ ($0.1\%$) at $\hat{\eta} \approx 0.80$:
$$N \ge \frac{0.80 \cdot 0.20}{(0.001)^2} = 1.6 \times 10^5 \text{ rays per angular state}$$

Production characterization requires $N = 2 \times 10^5$ to $5 \times 10^5$ rays per solar coordinate $(\theta_s, \phi_s)$.
