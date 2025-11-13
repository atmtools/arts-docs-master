import pyarts3 as pyarts
import numpy as np

# Create a simple matrix
x, y = np.meshgrid(np.linspace(-2, 2, 30), np.linspace(-2, 2, 30))
mat = pyarts.arts.Matrix(np.exp(-(x**2 + y**2)))

fig, ax = pyarts.plots.Matrix.plot(mat)
ax.set_title("2D Gaussian Matrix")