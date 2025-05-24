import matplotlib.pyplot as plt
import numpy as np

# Pipe length from 0 to L
L = 10
x = np.linspace(0, L, 500)

# Incompressible HGL drops linearly
HGL_incomp = 10 - (x / L) * 5  # Example: drops from 10m to 5m

# Compressible HGL drops slowly then steeply (simulating gas accelerating to Mach 1)
HGL_comp = 10 - (x / L)**1.5 * 8  # nonlinear drop, steeper toward end

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, HGL_incomp, label="Incompressible Flow", color="blue", linewidth=2)
plt.plot(x, HGL_comp, label="Compressible Flow", color="red", linestyle='--', linewidth=2)

plt.title("Hydraulic Gradient Line (HGL) Along Pipe")
plt.xlabel("Pipe Length (m)")
plt.ylabel("Hydraulic Head (m)")
plt.grid(True)
plt.legend()
plt.ylim(0, 11)
plt.show()
