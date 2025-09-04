import pyarts3 as pyarts
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 0.9)
y = np.arcsin(x)

xn = np.linspace(0, 1)
yn = pyarts.math.reinterp(y, pyarts.arts.interp.ArrayOfLagrange(x, xn, 1))

plt.plot(x, y, '-x')
plt.plot(xn, yn)