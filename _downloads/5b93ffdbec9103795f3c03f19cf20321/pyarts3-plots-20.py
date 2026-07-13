import pyarts3 as pyarts
import numpy as np

ant = pyarts.arts.sensor.GaussianAiryAntenna(np.linspace(0, 1, 11), 0.3, azi_grid_size=12)
ch = pyarts.arts.sensor.DiracChannel(100e9)
obsel = ant(ch, [1, 0, 0], [90, 0], pyarts.arts.planets.Earth.ellipsoid)

pyarts.plots.SensorObsel.plot(obsel, polar=True, point_spread=True)
pyarts.plots.SensorObsel.plot(obsel, point_spread=True, wrap_azimuth=True)
pyarts.plots.SensorObsel.plot(obsel, point_spread=True, frame="local")
pyarts.plots.SensorObsel.plot(obsel, point_spread=True, frame="local", type="cloud")
pyarts.plots.SensorObsel.plot(obsel, point_spread=True, frame="local", type="contour")