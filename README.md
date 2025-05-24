# Hydraulic Gradient Line (HGL) Plotter

This Python script visualizes the **Hydraulic Gradient Line (HGL)** along a horizontal pipe for both **incompressible** and **compressible** flow.

## 🔍 Description

The HGL represents the pressure head variation along the pipe. In this simulation:

- **Incompressible Flow** (e.g., water):
  - Assumes constant density
  - Head loss increases linearly with pipe length due to friction

- **Compressible Flow** (e.g., air at high velocity):
  - Includes the effect of increasing velocity and decreasing pressure
  - Shows a non-linear drop in head — shallow at first, then steep as the flow approaches Mach 1

This behavior is consistent with **Fanno flow** theory for adiabatic, 1D compressible flow in a constant-diameter pipe.

## 📈 Output

The script generates a graph showing:
- A **blue straight line**: Incompressible HGL
- A **red curved dashed line**: Compressible HGL
- X-axis: Pipe length (m)
- Y-axis: Hydraulic head (m)

## 🚀 How to Run

1. Make sure Python is installed (version 3+)
2. Install matplotlib if needed:
   ```bash
   pip install matplotlib

