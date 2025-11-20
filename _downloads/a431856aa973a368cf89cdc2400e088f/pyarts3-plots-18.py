import pyarts3 as pyarts
import numpy as np

x = np.linspace(-5, 5, 50)
y = np.linspace(-3, 3, 40)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2)/5)

propmat_matrix = pyarts.arts.PropmatMatrix(np.outer(Z.flatten(), [1, 0, 0, 0, 0, 0, 0]).reshape(40, 50, 7))
fig, ax = pyarts.plots.PropmatMatrix.plot(propmat_matrix)