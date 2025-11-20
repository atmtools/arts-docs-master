import pyarts3 as pyarts
import numpy as np

flux = pyarts.arts.DisortFlux()
flux.freq_grid = pyarts.arts.AscendingGrid(np.linspace(1e9, 1e12, 50))
flux.alt_grid = pyarts.arts.DescendingGrid(np.linspace(80e3, 0, 41))
alts_layers = 0.5 * (flux.alt_grid[:-1] + flux.alt_grid[1:])
flux.up = pyarts.arts.Matrix(np.outer(np.linspace(10, 100, 50), np.exp(-alts_layers/20e3)))
flux.down_diffuse = pyarts.arts.Matrix(np.outer(np.linspace(50, 150, 50), np.exp(-alts_layers/15e3)))
flux.down_direct = pyarts.arts.Matrix(np.outer(np.linspace(200, 300, 50),  np.exp(-alts_layers/10e3)))
fig, ax = pyarts.plots.DisortFlux.plot(flux)