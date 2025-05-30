import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # speed of light in meters per second

# Mass range (kg)
m = np.linspace(0, 1e-8, 500)  # very small masses for visualization

# Calculate Energy
E = m * c**2

# Plot
plt.figure(figsize=(8,5))
plt.plot(m, E, label=r'$E = mc^2$', color='red')

# Labels and title
plt.title('Energy vs Mass according to $E=mc^2$')
plt.xlabel('Mass (kg)')
plt.ylabel('Energy (Joules)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
