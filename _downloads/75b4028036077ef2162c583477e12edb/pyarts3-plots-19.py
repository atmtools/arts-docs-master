import pyarts3 as pyarts
import numpy as np

propmat_vec = pyarts.arts.PropmatVector(np.outer(np.exp(-np.linspace(0, 3, 100)), [1, 0, 0, 0, 0, 0, 0]))
fig, ax = pyarts.plots.PropmatVector.plot(propmat_vec)