import matplotlib.pyplot as plt
import pyarts3 as pa

plt.hist(pa.arts.random.normal_distribution(10000, 0, 10), bins=51, density=True)
plt.title("A plotting example")
plt.xlabel("Value")
plt.ylabel("Density")