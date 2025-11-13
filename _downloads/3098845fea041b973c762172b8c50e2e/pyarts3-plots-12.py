import pyarts3 as pyarts
import numpy as np

# Create a simplified sun object
sun = pyarts.arts.Sun()
sun.spectrum = pyarts.arts.Vector(np.ones(100) * 1e-3)  # Accepts Vector
sun.radius = 6.96e8  # meters
sun.distance = 1.496e11  # meters (1 AU)
sun.latitude = 0.0
sun.longitude = 0.0

pyarts.plots.Sun.plot(sun)