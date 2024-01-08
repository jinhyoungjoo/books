import open3d
from pytorch3d.io import load_obj, load_ply

PLY_FILE = "../data/cow.ply"
OBJ_FILE = "../data/cube_texture.obj"

print("Visualizing the PLY_FILE using Open3D")
mesh = open3d.io.read_triangle_mesh(PLY_FILE)
open3d.visualization.draw_geometries(
    [mesh], mesh_show_wireframe=True, mesh_show_back_face=True
)

print("Loading the PLY_FILE using Pytorch3D")
vertices, faces = load_ply(PLY_FILE)
print("Type of vertices:", type(vertices))
print("Type of faces:", type(faces))
print("Vertices:", vertices)
print("Faces:", faces)

print("Visualizing the OBJ_FILE using Open3D")
mesh = open3d.io.read_triangle_mesh(OBJ_FILE)
open3d.visualization.draw_geometries(
    [mesh], mesh_show_wireframe=True, mesh_show_back_face=True
)

print("Loading the OBJ_FILE using Pytorch3D")
vertices, faces, properties = load_obj(OBJ_FILE)
texture_images = getattr(properties, "texture_images")

print("Type of vertices:", type(vertices))
print("Type of faces:", type(faces))
print("Type of properties:", type(properties))
print("Type of texture images", type(texture_images))

print("Vertices:", vertices)
print("Faces:", faces)
print("Properties:", properties)
print("Texture Images:", texture_images["Skin"].shape)
