import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

atm_field = pyarts.arts.AtmField(toa=100e3)
atm_field["mag_u"] = 50e-6
atm_field["mag_v"] = 0
atm_field["mag_w"] = 3.14

fig = plt.figure(figsize=(14, 8))
fig, subs = pyarts.plots.AtmField.plot(atm_field, alts=np.linspace(0, 100e3), fig=fig, keys=["mag_u", "mag_v", "mag_w"])
subs[0].set_title("Magnetic profile u-component")
subs[1].set_title("Magnetic profile v-component")
subs[2].set_title("Magnetic profile w-component")
subs[0].set_ylabel("Altitude [m]")
[sub.set_xlabel("Field strength [T]") for sub in subs]
plt.show()