import os

import matplotlib.pyplot as plt
import numpy as np
import pyarts3 as pyarts

# Download catalogs
pyarts.data.download()

ws = pyarts.workspace.Workspace()

# %% Sampled frequency range
line_f0 = 118750348044.712
ws.freq_grid = np.linspace(-50e6, 50e6, 1001) + line_f0

# %% Species and line absorption
ws.abs_speciesSet(species=["O2-66"])
ws.ReadCatalogData()
ws.abs_bandsSelectFrequencyByLine(fmin=40e9, fmax=120e9)
ws.abs_bandsSetZeeman(species="O2-66", fmin=118e9, fmax=119e9)
ws.WignerInit()

# %% Use the automatic agenda setter for propagation matrix calculations
ws.spectral_propmat_agendaAuto()

# %% Grids and planet
ws.surf_fieldPlanet(option="Earth")
ws.surf_field[pyarts.arts.SurfaceKey("t")] = 295.0
ws.atm_fieldRead(
    toa=100e3, basename="planets/Earth/afgl/tropical/", missing_is_zero=1
)
ws.atm_fieldSchmidthFieldFromIGRF(time="2000-03-11 14:39:37")

# %% Checks and settings
ws.spectral_rad_transform_operatorSet(option="Tb")

# %% Core calculations
pos = [100e3, 0, 0]
los = [180.0, 0.0]
ws.ray_pathGeometric(pos=pos, los=los, max_stepsize=1000.0)
ws.rte_option = "constant"
ws.spectral_radClearskyEmission()
ws.spectral_radApplyUnitFromSpectralRadiance()

# %% Show results
fig, ax = pyarts.plot(ws.spectral_rad, freqs=(
    ws.freq_grid - line_f0) / 1e6)
[a.set_xlabel("Frequency offset [MHz]") for a in ax.flatten()]
[a.set_ylabel("Spectral radiance [K]") for a in ax.flatten()]
fig.suptitle(f"Zeeman effect of {round(line_f0 / 1e6)} MHz O$_2$ line")

if "ARTS_HEADLESS" not in os.environ:
    plt.show()

# %% Test

assert np.allclose(
    ws.spectral_rad[::100],
    np.array(
        [[ 2.27651282e+02,  4.26102060e-04,  1.02747352e-04,  5.68792738e-02],
         [ 2.30728866e+02,  6.60200882e-04,  1.59372185e-04,  7.04074714e-02],
         [ 2.34671712e+02,  1.16870303e-03,  2.82624380e-04,  9.34017354e-02],
         [ 2.40226524e+02,  2.61619467e-03,  6.34833158e-04,  1.40041532e-01],
         [ 2.49649981e+02,  9.75455461e-03,  2.39140470e-03,  2.69997141e-01],
         [ 2.09901775e+02,  2.41594007e+01,  1.73753634e+00,  5.52462292e-06],
         [ 2.49649415e+02,  9.75809646e-03,  2.39230231e-03, -2.70074598e-01],
         [ 2.40225433e+02,  2.61800016e-03,  6.35278628e-04, -1.40118090e-01],
         [ 2.34670137e+02,  1.16990381e-03,  2.82918000e-04, -9.34777147e-02],
         [ 2.30726819e+02,  6.61105602e-04,  1.59592410e-04, -7.04834216e-02],
         [ 2.27648772e+02,  4.26832612e-04,  1.02924697e-04, -5.69551084e-02]]
    ),
), "Values have drifted from expected results in spectral radiance"
