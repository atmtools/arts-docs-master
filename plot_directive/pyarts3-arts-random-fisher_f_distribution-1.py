import matplotlib.pyplot as plt
import pyarts3 as pa
import numpy as np

plt.hist(np.log(pa.arts.random.fisher_f_distribution(10000, 1.0, 1.0)), bins=50, density=True)
plt.title("A plotting example")
plt.xlabel("Log of Value")
plt.ylabel("Density")
plt.yscale("log")