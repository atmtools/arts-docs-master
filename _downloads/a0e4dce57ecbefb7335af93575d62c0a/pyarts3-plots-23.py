import pyarts3 as pyarts
import numpy as np

# Create a 2D radiance field
nx, ny = 40, 30
x = np.linspace(0, 2*np.pi, nx)
y = np.linspace(0, 2*np.pi, ny)
X, Y = np.meshgrid(x, y, indexing='ij')

stokes_mat = pyarts.arts.StokvecMatrix(np.zeros((nx, ny, 4)))
stokes_mat[:, :, 0] = np.sin(X) * np.cos(Y)  # I component

pyarts.plots.StokvecMatrix.plot(stokes_mat)