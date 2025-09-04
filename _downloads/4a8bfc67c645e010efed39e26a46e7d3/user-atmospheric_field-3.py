import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

h = pyarts.arts.SortedGriddedField3.fromxml("planets/Earth/afgl/tropical/p.xml").grids[0]
p = pyarts.arts.SortedGriddedField3.fromxml("planets/Earth/afgl/tropical/p.xml").data.flatten()

def h2p(alt, *args):
    return np.interp(alt, h, p)

atm_field = pyarts.arts.AtmField(toa=100e3)
atm_field["O3"] = lambda alt, lat, lon: 6e-6 if 25e3 < alt < 45e3 else 0
atm_field["p"] = h2p

fig = plt.figure(figsize=(14, 8))
fig, subs = pyarts.plots.AtmField.plot(atm_field, alts=np.linspace(0, 100e3), fig=fig, keys=["O3",'p'])
subs[0].set_title("Ozone profile using lambda-expression")
subs[0].legend().remove()
subs[1].set_title("Pressure profile using python function")
subs[0].set_ylabel("Altitude [m]")
subs[0].set_xlabel("O$_3$ VMR [-]")
subs[1].set_xlabel("Pressure [Pa]")
subs[1].set_xscale("log")
plt.show()