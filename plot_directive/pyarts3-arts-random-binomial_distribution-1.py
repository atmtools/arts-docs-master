import matplotlib.pyplot as plt
import pyarts3 as pa

plt.hist(pa.arts.random.binomial_distribution(10000, 10, 0.5), bins=11, density=True)
plt.title("A plotting example")
plt.xlabel("Value")
plt.ylabel("Density")