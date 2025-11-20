import pyarts3 as pyarts
import numpy as np

muelmat_vec = pyarts.arts.MuelmatVector(np.cos(np.linspace(0, 3, 1000)))
fig, ax = pyarts.plots.MuelmatVector.plot(muelmat_vec)