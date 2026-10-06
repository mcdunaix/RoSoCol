---
title: Receiver and Thermal Coupling
tags: [materials, receiver, pv-cells, thermal-management, pvt]
created: 2026-10-06
status: active
---

# Receiver and Thermal Coupling in Low-Concentration Systems

At geometric concentration ratios of $C_g = 1.5\times \text{ to } 3.0\times$, receiver thermal dissipation and electrical current extraction require explicit engineering to avoid efficiency degradation.

## 1. Photovoltaic Receiver Selection

For low-concentration non-imaging systems (LCPV, $C_g < 5\times$), standard silicon cells can operate efficiently provided series resistance $R_s$ is controlled.

### Candidate PV Technologies
1. **Interdigitated Back Contact (IBC) Monocrystalline Silicon**:
   - Zero front-metal grid shading.
   - Low series resistance handles $2\times \text{ to } 5\times$ concentrated current densities ($J_{\text{sc}} \approx 80 \text{ to } 180 \text{ mA/cm}^2$) with minimal resistive $I^2 R$ power loss.
   - High nominal efficiency ($\eta_{\text{STC}} \approx 23\% \text{ to } 24\%$).
2. **Standard Front-Contact Passivated Emitter and Rear Cell (PERC)**:
   - High resistive dissipation along thin front fingers under concentration.
   - Requires custom finger pitch redesign for $C > 2\times$.
3. **Cylindrical Flexible CIGS / Amorphous Silicon**:
   - Can conform directly around the central core of toroidal collectors [[22-Toroidal-and-Annular-Architectures]].
   - Lower baseline efficiency ($\eta \approx 14\% \text{ to } 16\%$), but eliminates mechanical joints.

## 2. Thermal Dissipation Modeling

Under concentration $C_{\text{flux}}$, the incident optical flux on the cell is:

$$q_{\text{incident}} = C_{\text{flux}} \cdot \eta_{\text{opt}} \cdot I_{\text{DNI}}$$

With $I_{\text{DNI}} = 1000 \text{ W/m}^2$, $C_{\text{flux}} = 2.5\times$, and $\eta_{\text{opt}} = 0.80$:
$$q_{\text{incident}} = 2000 \text{ W/m}^2 = 0.20 \text{ W/cm}^2$$

Assuming cell electrical efficiency $\eta_e = 20\%$, the thermal load rejected into the receiver substrate is:

$$q_{\text{thermal}} = q_{\text{incident}} \cdot (1 - \eta_e) = 1600 \text{ W/m}^2$$

### Temperature Rise and Passive Heat Sinking
The steady-state temperature rise above ambient is:

$$\Delta T = T_{\text{cell}} - T_{\text{ambient}} = q_{\text{thermal}} \cdot A_{\text{cell}} \cdot R_{\text{th, total}}$$

Where thermal resistance is the series sum:
$$R_{\text{th, total}} = R_{\text{cell-substrate}} + R_{\text{TIM}} + R_{\text{heatsink-air}}$$

For passive cooling without fans or pumps:
- An anodized aluminum extruded pin-fin heatsink operating under natural convection provides $h_{\text{conv}} \approx 8 \text{ to } 15 \text{ W/(m}^2\cdot\text{K)}$.
- For $C_g \le 3.0\times$, a heatsink surface area ratio $A_{\text{sink}} / A_{\text{cell}} \ge 8:1$ maintains cell operating temperatures at $\Delta T \le 25^\circ\text{C}$ above ambient ($T_{\text{cell}} \le 65^\circ\text{C}$ on a $40^\circ\text{C}$ summer day).
- This keeps cell efficiency loss within acceptable bounds ($\Delta\eta / \eta \le 10\%$, given the Si temperature coefficient $\gamma_P \approx -0.38\% / ^\circ\text{C}$).

## 3. Hybrid Photovoltaic-Thermal (PV/T) Architecture

In a rotational collector with an axial cylindrical receiver, the central core naturally houses a fluid conduit:
- A copper absorber tube is bonded with thermal paste to the rear of the curved PV array.
- Water, glycol, or heat-transfer oil circulates through the vertical axis without requiring rotational swivel joints.
- Synergistic outcome: Co-generates domestic hot water ($45^\circ\text{C} \text{ to } 65^\circ\text{C}$) while cooling the PV cells to maximize electrical yield.
