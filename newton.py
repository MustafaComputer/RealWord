import matplotlib.pyplot as plt
import numpy as np

# Newton's Second Law: F = m * a  => a = F / m

# 1. Acceleration vs Mass (F = constant)
F1 = 10  # constant force in Newtons
mass = np.linspace(1, 10, 100)  # mass from 1 kg to 10 kg
acceleration_mass = F1 / mass

# 2. Acceleration vs Force (m = constant)
m2 = 5  # constant mass in kg
force = np.linspace(0, 20, 100)  # force from 0 to 20 N
acceleration_force = force / m2

# Create the plots
plt.figure(figsize=(12, 5))

# Plot 1: Acceleration vs Mass
plt.subplot(1, 2, 1)
plt.plot(mass, acceleration_mass, color='blue')
plt.title("Acceleration vs Mass (F = 10 N)")
plt.xlabel("Mass (kg)")
plt.ylabel("Acceleration (m/s²)")
plt.grid(True)

# Plot 2: Acceleration vs Force
plt.subplot(1, 2, 2)
plt.plot(force, acceleration_force, color='green')
plt.title("Acceleration vs Force (m = 5 kg)")
plt.xlabel("Force (N)")
plt.ylabel("Acceleration (m/s²)")
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()
