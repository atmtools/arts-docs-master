import pyarts3 as pyarts
import numpy as np

# Create a geographic field
lats = pyarts.arts.LatGrid(np.linspace(-90, 90, 20))
lons = pyarts.arts.LonGrid(np.linspace(-180, 175, 36))
lon_mesh, lat_mesh = np.meshgrid(lons, lats)

# Example: distance from equator
data = pyarts.arts.Matrix(np.abs(lat_mesh))

field = pyarts.arts.GeodeticField2()
field.grids = (lats, lons)
field.data = data
field.dataname = "Distance from Equator"

pyarts.plots.GeodeticField2.plot(field)