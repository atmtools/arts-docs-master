import pyarts3 as pyarts
import numpy as np

ws = pyarts.Workspace()
ws.measurement_sensorSimpleGaussian(std = 10e6, pos = [100e3, 0, 0], los = [180.0, 0.0],
                                    freq_grid = np.linspace(-50e6, 50e6, 101))
pyarts.plots.ArrayOfSensorObsel.plot(ws.measurement_sensor)