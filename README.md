# Y-12 National Security Complex TAP Innovation Challenge Prototype

This repository contains the dynamic path-tracking script and conceptual framework developed by my team during the Fall 2026 Y-12 Technology Accelerator Program (TAP) Innovation Challenge. Our team designed a 3D digital twin prototype of a facility processing bay to streamline As Low As Reasonably Achievable (ALARA) occupational route planning. The OpenMC geometry code is not included because we didn't have enough time to combine them.

## The Challenge Constraint
Faced with a strict **4-hour time limit**, our multi-disciplinary team rapidly conceptualized a health physics simulation. To deliver a functional project, we implemented specific practical engineering and geometric simplifications:
- **Simplified Biometric Geometry:** Modeled humans as uniform cylinders rather than complex anthropomorphic shapes.
- **Homogeneous Shielding Factors:** Assumed an idealized, uniform human tissue shielding factor equal to 1.
- **Whole-Body Dose Assumptions:** Omitted localized or concentrated radiological impacts on specific limbs.
- **Kinematic Simplifications:** Maintained a constant worker velocity along discrete, straight-line walking trajectories.

## Technical Implementation
- **Dynamic Trajectory Interpolation (Main Script):** Built a standalone Python script utilizing linear interpolation routines to dynamically evaluate, calculate, and integrate cumulative worker radiation dose profiles along changing trajectories.
- **Data Visualization:** Generated Matplotlib visualizations tracking localized dose levels against specific time steps and plotting the total accumulated curve.
- **Conceptual OpenMC Framework:** Designed the parallel workflow requirements for fixed-source radiation geometries, material properties, and spatial tracking matrices to generate ambient dose-rate fields for future programmatic integration.
  
## Prerequisites & Run Environment
The analysis and trajectory tracking script requires a standard Python 3 interpreter equipped with:
- `numpy`
- `matplotlib`
- `openmc` (or pre-computed spatial matrix data frames)

