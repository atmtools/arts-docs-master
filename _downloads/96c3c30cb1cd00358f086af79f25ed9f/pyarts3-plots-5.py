import pyarts3 as pyarts
import numpy as np

ws = pyarts.Workspace()

ws.atm_fieldRead(toa=100e3, basename="planets/Earth/afgl/tropical/")

pyarts.plots.AtmField.plot(ws.atm_field, keys=["p", "t"])