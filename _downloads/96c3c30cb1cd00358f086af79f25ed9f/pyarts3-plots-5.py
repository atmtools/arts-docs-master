import pyarts3 as pyarts
import numpy as np

# Create a frequency grid
freqs = pyarts.arts.AscendingGrid(np.logspace(9, 12, 20))

pyarts.plots.AscendingGrid.plot(freqs)