import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

lines = pyarts.arts.AbsorptionBands.fromxml("lines/O2-66.xml")
freq = np.linspace(20e9, 140e9, 1001)
lines.keep_frequencies(freq[0], freq[-1])
f, a = pyarts.plots.AbsorptionBands.plot(lines, mode="important fill bands", freqs=freq, fig=plt.figure(figsize=(16, 5)))
a.set_yscale("log")
a.set_xlabel("Frequency [GHz]")
a.set_xticks(np.linspace(20, 140, 7) * 1e9, np.linspace(20, 140, 7))
a.set_ylabel("Absorption [1/m]")
a.legend()
a.set_title("O$_2$ line-by-line absorption 20-140 GHz separated by bands")