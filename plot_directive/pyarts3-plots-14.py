import pyarts3 as pyarts
import numpy as np

# Create a longitude grid
lons = pyarts.arts.LonGrid(np.linspace(-180, 175, 36))

pyarts.plots.LonGrid.plot(lons, polar=True)