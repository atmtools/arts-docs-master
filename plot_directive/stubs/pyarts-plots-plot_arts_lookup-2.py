from os.path import join, dirname
import matplotlib.pyplot as plt
import pyarts
from pyarts.arts import ArrayOfArrayOfSpeciesTag, SpeciesTag

lookup_file = join(dirname(pyarts.__file__), '../test/plots/reference',
                   'abs_lookup_small.xml')
fig, ax = pyarts.plots.plot_arts_lookup(
    pyarts.xml.load(lookup_file),
    species=ArrayOfArrayOfSpeciesTag([[SpeciesTag("N2O")],
                                      [SpeciesTag("O3")]]),
    opacity=False)

fig.suptitle('Lookup table absorption cross sections [m$^2$]')
fig.subplots_adjust(top=0.88)
plt.show()