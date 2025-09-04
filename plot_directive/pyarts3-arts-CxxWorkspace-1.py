import pyarts3 as pyarts
import numpy as np

ws = pyarts.Workspace()

ws.atmospheric_fieldRead(toa=100e3, basename="planets/Earth/afgl/tropical/")
ws.surface_fieldEarth()
ws.ray_path_observer_agendaSetGeometric(
    add_crossings=True, remove_non_crossings=True
)
ws.ray_path_observersFieldProfilePseudo2D(nup=3, nlimb=3, ndown=3)
ws.ray_path_fieldFromObserverAgenda()

f, a = None, None
for x in ws.ray_path_field:
    f, a = pyarts.plots.ray_path.polar_ray_path(
        x, draw_za_aa=True, draw_map=False, fig=f, axes=a
    )