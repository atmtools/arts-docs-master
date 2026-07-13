import pyarts3 as pyarts
import numpy as np

# Create a gridded field
freqs = pyarts.arts.AscendingGrid(np.linspace(1e9, 1e12, 100))
data = pyarts.arts.Vector(np.exp(-((freqs - 5e11)/1e11)**2))

field = pyarts.arts.SortedGriddedField1()
field.grids = (freqs,)
field.data = data
field.gridnames = ("Frequency [Hz]",)
field.dataname = "Response"

pyarts.plots.SortedGriddedField1.plot(field)