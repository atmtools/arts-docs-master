import pyarts3 as pyarts
import numpy as np

x = np.linspace(0, 10, 50)
y = np.linspace(0, 5, 30)
X, Y = np.meshgrid(x, y, indexing='ij')
Z = np.sin(X) * np.cos(Y)

sgf2 = pyarts.arts.SortedGriddedField2()
sgf2.grids = [pyarts.arts.AscendingGrid(x), pyarts.arts.AscendingGrid(y)]
sgf2.data = pyarts.arts.Matrix(Z)

fig, ax = pyarts.plots.SortedGriddedField2.plot(sgf2)