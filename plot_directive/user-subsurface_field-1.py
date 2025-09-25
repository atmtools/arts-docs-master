import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

subsurf_field = pyarts.arts.SubsurfaceField(bottom_depth=-1.0)
subsurf_field["t"] = 295
subsurf_field["rho"] = 0.977

fig = plt.figure(figsize=(14, 8))
fig, subs = pyarts.plots.SubsurfaceField.plot(subsurf_field, alts=np.linspace(-1, 0), fig=fig, keys=["t"])
subs[0].set_title("Temperature profile")
subs[1].set_title("Density profile")
subs[0].set_ylabel("Altitude [m]")
[sub.set_xlabel("Field strength [T]") for sub in subs]
plt.show()