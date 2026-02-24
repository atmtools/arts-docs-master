import matplotlib.pyplot as plt
import pyarts3 as pa

plt.hist(pa.arts.random.poisson_distribution(10000, 250), bins=50, density=True)
plt.title("A plotting example")
plt.xlabel("Value")
plt.ylabel("Density")
plt.yscale("log")