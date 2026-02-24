import matplotlib.pyplot as plt
import pyarts3 as pa

plt.hist(pa.arts.random.uniform_int_distribution(10000, 0, 9), bins=10, density=True)
plt.title("A plotting example")
plt.xlabel("Value")
plt.ylabel("Density")