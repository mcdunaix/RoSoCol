#!/usr/bin/env python3
"""
CPC Profile Generator for RoSoCol (Rotational Omnidirectional Solar Collector)

Calculates the analytical coordinates for 2D and 3D Compound Parabolic
Concentrators (CPC) and Dielectric Concentrators (DTIRC) according to
Winston-Welford edge-ray formulations.

Can export coordinates to CSV and generate a 3D Wavefront .OBJ mesh
of the revolved solid of revolution for CAD import or ray-tracing.
"""

import math
import argparse
import sys
import os
import csv


def calculate_cpc_profile(a_prime, theta_a_deg, truncation_ratio=1.0, n=1.0, num_points=100):
    """
    Calculate 2D profile coordinates (y, z) for a Winston CPC.

    Parameters:
    -----------
    a_prime : float
        Half-width (or radius) of the absorber / receiver.
    theta_a_deg : float
        Acceptance half-angle in degrees.
    truncation_ratio : float
        Height truncation factor in range (0.1, 1.0].
    n : float
        Refractive index of dielectric medium (1.0 for hollow/air).
    num_points : int
        Number of points along the parabolic curve.

    Returns:
    --------
    dict containing metadata, profile points [(y, z)], and key metrics.
    """
    theta_a = math.radians(theta_a_deg)
    sin_theta = math.sin(theta_a)
    cos_theta = math.cos(theta_a)
    tan_theta = math.tan(theta_a)

    if sin_theta <= 0 or sin_theta >= 1.0:
        raise ValueError("Acceptance angle must be between 0 and 90 degrees exclusive.")

    # Geometric concentration ratio
    # 2D ideal: C_2d = n / sin(theta_a)
    # 3D ideal: C_3d = (n / sin(theta_a))^2
    c_2d_ideal = n / sin_theta
    c_3d_ideal = (n / sin_theta) ** 2

    # Untruncated aperture radius
    a_untruncated = a_prime / sin_theta
    # Untruncated height L
    l_untruncated = (a_prime * (1.0 + sin_theta) * cos_theta) / (sin_theta ** 2)

    # Truncated height
    l_target = l_untruncated * truncation_ratio

    # Parameter psi ranges from theta_a + pi/2 (receiver) to 2*theta_a (aperture)
    # At receiver edge (y = a_prime, z = 0): psi = theta_a + pi/2
    # At top aperture (y = a, z = L): psi = 2*theta_a
    psi_start = theta_a + (math.pi / 2.0)
    psi_end = 2.0 * theta_a

    # Parametric equations in polar coordinates from focal point F = (a_prime, 0):
    # Focal parameter: f_prime = a_prime * (1.0 + sin_theta)
    # rho(psi) = 2 * f_prime / (1 - cos(psi))
    # y(psi) = -a_prime + rho(psi) * sin(psi - theta_a)
    # z(psi) = rho(psi) * cos(psi - theta_a)
    f_prime = a_prime * (1.0 + sin_theta)

    points = []
    for i in range(num_points):
        t = i / (num_points - 1)
        psi = psi_start + t * (psi_end - psi_start)

        rho = (2.0 * f_prime) / (1.0 - math.cos(psi))
        y = -a_prime + rho * math.sin(psi - theta_a)
        z = rho * math.cos(psi - theta_a)

        # Truncate if z exceeds target length
        if z > l_target:
            if len(points) > 0 and points[-1][1] < l_target:
                prev_y, prev_z = points[-1]
                dz = z - prev_z
                if dz > 1e-9:
                    frac = (l_target - prev_z) / dz
                    y_exact = prev_y + frac * (y - prev_y)
                    points.append((y_exact, l_target))
            break

        points.append((y, z))

    if not points:
        points.append((a_prime, 0.0))

    actual_a = points[-1][0]
    actual_l = points[-1][1]
    actual_c_2d = actual_a / a_prime
    actual_c_3d = (actual_a / a_prime) ** 2

    return {
        "a_prime": a_prime,
        "theta_a_deg": theta_a_deg,
        "n": n,
        "truncation_ratio": truncation_ratio,
        "untruncated_a": a_untruncated,
        "untruncated_height": l_untruncated,
        "actual_a": actual_a,
        "actual_height": actual_l,
        "c_2d": actual_c_2d,
        "c_3d": actual_c_3d,
        "c_2d_ideal": c_2d_ideal,
        "c_3d_ideal": c_3d_ideal,
        "points": points,
    }


def export_csv(result, filepath):
    """Export profile coordinates to CSV."""
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["# RoSoCol Parametric CPC Profile"])
        writer.writerow(["# Absorber Radius (mm)", result["a_prime"]])
        writer.writerow(["# Acceptance Angle (deg)", result["theta_a_deg"]])
        writer.writerow(["# Geometric 3D Concentration", f"{result['c_3d']:.4f}"])
        writer.writerow(["# Height (mm)", f"{result['actual_height']:.4f}"])
        writer.writerow(["radius_mm", "z_height_mm"])
        for y, z in result["points"]:
            writer.writerow([f"{y:.6f}", f"{z:.6f}"])


def export_obj_mesh(result, filepath, azimuthal_steps=64):
    """
    Generate a 3D Wavefront .OBJ mesh by revolving the 2D profile
    around the z-axis.
    """
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    points = result["points"]
    num_profile_pts = len(points)

    with open(filepath, mode="w") as f:
        f.write("# RoSoCol 3D Revolved CPC Solid of Revolution\n")
        f.write(f"# Absorber Radius: {result['a_prime']} mm\n")
        f.write(f"# Acceptance Angle: {result['theta_a_deg']} deg\n")
        f.write(f"# 3D Concentration: {result['c_3d']:.3f}x\n\n")

        # Write vertices: ring by ring along z
        for y, z in points:
            for j in range(azimuthal_steps):
                phi = (2.0 * math.pi * j) / azimuthal_steps
                vx = y * math.cos(phi)
                vy = y * math.sin(phi)
                vz = z
                f.write(f"v {vx:.6f} {vy:.6f} {vz:.6f}\n")

        f.write("\n")

        # Write quad faces between adjacent rings
        for ring in range(num_profile_pts - 1):
            ring_start = ring * azimuthal_steps + 1
            next_ring_start = (ring + 1) * azimuthal_steps + 1

            for j in range(azimuthal_steps):
                next_j = (j + 1) % azimuthal_steps

                v1 = ring_start + j
                v2 = ring_start + next_j
                v3 = next_ring_start + next_j
                v4 = next_ring_start + j

                # Outward-facing quad
                f.write(f"f {v1} {v2} {v3} {v4}\n")


def main():
    parser = argparse.ArgumentParser(
        description="RoSoCol CPC Analytical Profile and Mesh Generator"
    )
    parser.add_argument(
        "--absorber_radius",
        type=float,
        default=25.0,
        help="Receiver radius / half-width in mm (default: 25.0)",
    )
    parser.add_argument(
        "--acceptance_angle",
        type=float,
        default=30.0,
        help="Acceptance half-angle theta_a in degrees (default: 30.0)",
    )
    parser.add_argument(
        "--truncation",
        type=float,
        default=0.6,
        help="Truncation ratio (0.1 to 1.0, default: 0.6)",
    )
    parser.add_argument(
        "--refractive_index",
        type=float,
        default=1.0,
        help="Medium refractive index n (default: 1.0)",
    )
    parser.add_argument(
        "--points",
        type=int,
        default=100,
        help="Number of points along the profile (default: 100)",
    )
    parser.add_argument(
        "--csv",
        type=str,
        default=None,
        help="Path to export coordinate profile CSV",
    )
    parser.add_argument(
        "--obj",
        type=str,
        default=None,
        help="Path to export 3D revolved .OBJ mesh",
    )

    args = parser.parse_args()

    res = calculate_cpc_profile(
        a_prime=args.absorber_radius,
        theta_a_deg=args.acceptance_angle,
        truncation_ratio=args.truncation,
        n=args.refractive_index,
        num_points=args.points,
    )

    print("=" * 60)
    print(" RoSoCol Non-Imaging Optical Profile Summary")
    print("=" * 60)
    print(f"Receiver Radius (a'):         {res['a_prime']:.2f} mm")
    print(f"Acceptance Half-Angle:        {res['theta_a_deg']:.2f} deg")
    print(f"Refractive Index (n):         {res['n']:.3f}")
    print(f"Truncation Factor:            {res['truncation_ratio']:.2f}")
    print("-" * 60)
    print(f"Untruncated Aperture Radius:  {res['untruncated_a']:.2f} mm")
    print(f"Untruncated Total Height:     {res['untruncated_height']:.2f} mm")
    print(f"Actual Aperture Radius:       {res['actual_a']:.2f} mm")
    print(f"Actual Total Height:          {res['actual_height']:.2f} mm")
    print("-" * 60)
    print(f"2D Concentration Ratio:       {res['c_2d']:.3f}x (ideal: {res['c_2d_ideal']:.3f}x)")
    print(f"3D Geometric Concentration:   {res['c_3d']:.3f}x (ideal: {res['c_3d_ideal']:.3f}x)")
    print("=" * 60)

    if args.csv:
        export_csv(res, args.csv)
        print(f"Saved CSV profile to: {args.csv}")

    if args.obj:
        export_obj_mesh(res, args.obj)
        print(f"Saved 3D OBJ mesh to: {args.obj}")


if __name__ == "__main__":
    main()
