import pyarts3 as pyarts
import numpy as np

# Create a geographic field
lats = pyarts.arts.Vector(np.linspace(-90, 90, 20))
lons = pyarts.arts.Vector(np.linspace(-180, 175, 36))
lon_mesh, lat_mesh = np.meshgrid(lons, lats)

# Example: distance from equator
data = pyarts.arts.Matrix(np.abs(lon_mesh))

field = pyarts.arts.GriddedField2()
field.grids = (lats, lons)
field.data = data
field.dataname = "Distance from Equator"

pyarts.plots.GriddedField2.plot(field)