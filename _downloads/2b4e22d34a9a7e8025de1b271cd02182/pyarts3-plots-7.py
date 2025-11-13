import pyarts3 as pyarts
import numpy as np

# Create a latitude grid
lats = pyarts.arts.LatGrid(np.linspace(-90, 90, 19))

pyarts.plots.LatGrid.plot(lats, polar=True)