extends MeshInstance

#var tmpMesh = Mesh.new()
#
#func _ready():
#	var st = SurfaceTool.new()
#	st.begin(Mesh.PRIMITIVE_TRIANGLE_STRIP)
#	st.add_vertex(Vector3(-1, 0 , -1))
#	st.add_vertex(Vector3(1,0,-1))
#	st.add_vertex(Vector3(0,0,1))
##	st.add_vertex(Vector3(2,0,1))
#	st.commit(tmpMesh)
#
#
#	self.mesh = tmpMesh
#
#

var vertices = PoolVector3Array()

func _ready():
	vertices.push_back(Vector3(-1,-1,-1))
	vertices.push_back(Vector3(1,0,-1))
	vertices.push_back(Vector3(0,0,1))


	var tmpMesh = ArrayMesh.new()
	var arrays = Array()
	arrays.resize(ArrayMesh.ARRAY_MAX)
	arrays[ArrayMesh.ARRAY_VERTEX] = vertices

	tmpMesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
	self.mesh = tmpMesh






	get_node("../CollisionShape").shape = self.mesh.create_trimesh_shape()

	
#	print(get_node("../CollisionShape").shape.points,'     ', self.mesh.get_faces())
