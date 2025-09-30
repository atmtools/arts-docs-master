import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

subsurf_field = pyarts.arts.SubsurfaceField(bottom_depth=-1)
subsurf_field["t"] = 295
subsurf_field["rho"] = 0.977

fig = plt.figure(figsize=(14, 8))
fig, subs = pyarts.plots.SubsurfaceField.plot(subsurf_field, alts=np.linspace(-1, 0), fig=fig, keys=["t", "rho"])
subs[0].set_title("Temperature profile")
subs[1].set_title("Density profile")
subs[0].set_ylabel("Depth [m]")
subs[0].set_xlabel("Temperature [K]")
subs[1].set_xlabel("Density [kg/m$^3$]")
plt.show()