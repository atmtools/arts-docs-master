import pyarts3 as pyarts
import numpy as np

# Create zenith angles from 0° (up) to 180° (down)
zenith = pyarts.arts.ZenithGrid(np.linspace(0, 180, 19))

pyarts.plots.ZenithGrid.plot(zenith, polar=True)