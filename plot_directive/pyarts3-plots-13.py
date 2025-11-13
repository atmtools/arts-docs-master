import pyarts3 as pyarts
import numpy as np

# Create a simple vector
x = np.linspace(0, 2*np.pi, 50)
vec = pyarts.arts.Vector(np.sin(x))

pyarts.plots.Vector.plot(vec, xgrid=pyarts.arts.convert.rad2deg(x))