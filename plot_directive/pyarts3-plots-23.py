import pyarts3 as pyarts
import numpy as np

stokvec_vec = pyarts.arts.StokvecVector(np.outer(np.sin(np.linspace(0, 3, 100)), [1, 0.5, 0.3, 0.1]))
fig, ax = pyarts.plots.StokvecVector.plot(stokvec_vec)