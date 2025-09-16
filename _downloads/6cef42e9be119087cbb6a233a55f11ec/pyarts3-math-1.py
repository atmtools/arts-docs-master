import pyarts3 as pyarts
import numpy as np
import matplotlib.pyplot as plt

x = [0.1, 0.4, 0.6, 0.9]
y = np.arcsin(x)

xn = 0.5
yn = pyarts.math.interp(y, pyarts.arts.interp.LagrangeCyclic(x, xn, 1))

plt.plot(x, y, '-x')
plt.plot([xn], [yn], '*')