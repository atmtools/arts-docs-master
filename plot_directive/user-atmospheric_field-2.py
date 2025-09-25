import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

atm_field = pyarts.arts.AtmField(toa=100e3)
atm_field["t"] = pyarts.arts.GeodeticField3.fromxml("planets/Earth/afgl/tropical/t.xml")
atm_field["O2"] = pyarts.arts.GeodeticField3.fromxml("planets/Earth/afgl/tropical/O2.xml")
atm_field["H2O"] = pyarts.arts.GeodeticField3.fromxml("planets/Earth/afgl/tropical/H2O.xml")

fig = plt.figure(figsize=(14, 8))
fig, subs = pyarts.plots.AtmField.plot(atm_field, alts=np.linspace(0, 100e3), fig=fig, keys=["t", "O2", "H2O"])
subs[0].set_title("Temperature profile")
subs[1].set_title("O$_2$ VMR profile")
subs[2].set_title("H$_2$O VMR profile")
subs[0].set_ylabel("Altitude [m]")
subs[0].set_xlabel("Temperature [K]")
subs[1].set_xlabel("O$_2$ VMR [-]")
subs[2].set_xlabel("H$_2$O VMR [-]")
subs[2].set_xscale("log")
plt.show()