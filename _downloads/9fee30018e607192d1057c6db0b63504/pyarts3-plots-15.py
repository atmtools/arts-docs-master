import pyarts3 as pyarts

mag_angles = pyarts.arts.zeeman.MagneticAngles([0, 1, 2], [3, 4])
fig, ax = pyarts.plots.MagneticAngles.plot(mag_angles)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()