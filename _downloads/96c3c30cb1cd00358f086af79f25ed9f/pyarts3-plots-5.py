import pyarts3 as pyarts
import numpy as np

# Create azimuth angles (compass directions)
azimuth = pyarts.arts.AzimuthGrid(np.linspace(0, 360, 13)[:-1])

fig, ax = pyarts.plots.AzimuthGrid.plot(azimuth, polar=True)
ax.set_xlabel("Index")
ax.set_ylabel("Azimuth Angle [°]")
ax.set_title("Azimuth Grid")
ax.set_ylim(0, 360)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1.2)
ax.set_theta_zero_location("N")  # 0° at North (top)
ax.set_theta_direction(-1)  # Clockwise (East = 90° clockwise from North)