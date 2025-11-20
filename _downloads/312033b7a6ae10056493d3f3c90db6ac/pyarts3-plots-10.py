import pyarts3 as pyarts
import numpy as np

radiance = pyarts.arts.DisortRadiance()
radiance.freq_grid = pyarts.arts.AscendingGrid(np.linspace(1e9, 1e12, 50))
radiance.alt_grid = pyarts.arts.DescendingGrid(np.linspace(80e3, 0, 41))
radiance.azi_grid = pyarts.arts.AziGrid(np.linspace(0, 330, 12))
radiance.zen_grid = pyarts.arts.ZenGrid(np.linspace(0, 180, 17))
radiance.data = pyarts.arts.Tensor4(np.random.randn(50, 41, 12, 17) * 10 + 100 * np.sin(np.radians(radiance.zen_grid))[None, None, None, :])
fig, ax = pyarts.plots.DisortRadiance.plot(radiance)