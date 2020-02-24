import numpy as np
from fury.primitive import prim_sphere
from fury import window, utils
from fury.io import save_polydata, load_polydata
from fury.utils import vtk

verts, faces = prim_sphere('symmetric362')
verts.shape == (362, 3)

faces.shape == (720, 3)
print(verts, faces)
my_polydata = vtk.vtkPolyData()
my_vertices = np.array(verts)
my_triangles = np.array(faces)
utils.set_polydata_vertices(my_polydata, my_vertices)
utils.set_polydata_triangles(my_polydata, my_triangles)
file_name = "my_cube.vtk"
save_polydata(my_polydata, file_name)
print("Surface saved in " + file_name)
cube_polydata = load_polydata(file_name)
cube_vertices = utils.get_polydata_vertices(cube_polydata)
colors = cube_vertices * 255
utils.set_polydata_colors(cube_polydata, colors)

print("new surface colors")
print(utils.get_polydata_colors(cube_polydata))
cube_actor = utils.get_actor_from_polydata(cube_polydata)


scene = window.Scene()
scene.add(cube_actor)
scene.set_camera(position=(10, 5, 7), focal_point=(0.5, 0.5, 0.5))
scene.zoom(3)
window.record(scene, out_path='sakshi.png', size=(600, 600))