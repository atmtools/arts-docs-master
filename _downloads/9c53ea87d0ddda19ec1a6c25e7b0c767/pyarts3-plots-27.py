import pyarts3 as pyarts
import numpy as np

f = pyarts.arts.SurfaceField()
f.ellipsoid = [1.0, 1]
f['t'] = lambda lat, lon: 280 + 0.5 * lat**2 - 10 * lon
pyarts.plots.SurfaceField.plot(f)