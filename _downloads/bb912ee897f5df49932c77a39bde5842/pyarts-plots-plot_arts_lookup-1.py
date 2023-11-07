from os.path import join, dirname
import matplotlib.pyplot as plt
import pyarts

lookup_file = join(dirname(pyarts.__file__), '../test/plots/reference',
                   'abs_lookup_small.xml')
fig, ax = pyarts.plots.plot_arts_lookup(pyarts.xml.load(lookup_file))

fig.suptitle('Lookup table opacities')
fig.subplots_adjust(top=0.88)
plt.show()