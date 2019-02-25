extends MeshInstance

var all_arr = []
var tmpMesh = Mesh.new()
var L_and_H_points = []

var dis_arr = []
func _ready():
	dis_arr = [Vector3(100,10,100), Vector3(900, -10, 900)]
	all_arr = generate_vertexes()
	all_arr = deform_mesh(all_arr, dis_arr)
	self.mesh = gen_mesh(all_arr)
	print(3)
#	get_node("../StaticBody/CollisionShape").shape.points = coll(all_arr)
#	print(self.mesh.get_faces())
#var n = 0
#func _process(delta):
#	if n == 1:
#		get_node("../StaticBody/CollisionShape").shape.points = coll(all_arr)
	

func generate_vertexes():
	var a_arr = []
	for i in range(1000):
		var h_arr = []
		for j in range(1000):
			h_arr.append(Vector3(i, 0, j))
		a_arr.append(h_arr)
	return(a_arr)
	
func deform_mesh(arr, displace_arr):
	var result = PoolVector3Array()
	for i in range(1000):
		for j in range(1000):
			var r1 = 0
			var r2 = 0
			r2 = 50 - abs(arr[i][j].x - 50)
			r1 = 50 - abs(arr[i][j].z - 50)
			var k = 1
			if r1 < r2:
				k = r1
			else:
				k = r2
			k = k/50
			arr[i][j].y += ((Vector2(arr[i][j].x, arr[i][j].z)).distance_to(Vector2(displace_arr[0].x, displace_arr[0].z)) / 100 - (Vector2(arr[i][j].x, arr[i][j].z).distance_to(Vector2(displace_arr[1].x, displace_arr[1].z)) / 100))  * 1 * k
#	result.resize(6000000)
#	print(1)
	for i in range(999):
#		print(result.size())
		for j in range(999):
			result.append(arr[i+1][j])
			result.append(arr[i][j+1])
			result.append(arr[i][j])
			result.append(arr[i+1][j+1])
			result.append(arr[i][j+1])
			result.append(arr[i+1][j])
#	print("benis")
	return(result)

func gen_mesh(Arr2):
	print(1)
	var mat = self.get_surface_material(0)
#	var st = SurfaceTool.new()
	var tmpMesh = ArrayMesh.new()
	var arrays = Array()
	arrays.resize(ArrayMesh.ARRAY_MAX)
	arrays[ArrayMesh.ARRAY_VERTEX] = Arr2

	tmpMesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
	print(2)
	return(tmpMesh)

	


func coll(arr):
	var result = PoolVector3Array()
	for i in range(1000):
		for j in range(1000):
			result.append(arr[i][j])
	return(result)



	
func print_arr():
	for i in range(1000):
		for j in range(1000):
			print(all_arr[i][j])
			
			
			
	