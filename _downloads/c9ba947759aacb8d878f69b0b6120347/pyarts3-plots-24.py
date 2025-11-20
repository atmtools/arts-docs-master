import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

subsurf_field = pyarts.arts.SubsurfaceField(bottom_depth=-1)
subsurf_field["t"] = lambda alt, lat, lon: 295 + 5 * alt * 10
subsurf_field["rho"] = lambda alt, lat, lon: 0.977 - 0.001 * alt

fig = plt.figure(figsize=(14, 8))
fig, subs = pyarts.plots.SubsurfaceField.plot(subsurf_field, alts=np.linspace(-1, 0), fig=fig, keys=["t", "rho"])
subs.flatten()[0].set_title("Temperature profile")
subs.flatten()[1].set_title("Density profile")
subs.flatten()[0].set_ylabel("Depth [m]")
subs.flatten()[0].set_xlabel("Temperature [K]")
subs.flatten()[1].set_xlabel("Density [kg/m$^3$]")