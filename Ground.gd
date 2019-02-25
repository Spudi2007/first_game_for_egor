extends MeshInstance

# class member variables go here, for example:
# var a = 2 
var material = self.get_surface_material(0)
var a = Vector3(-128, 30, 128)
var b = Vector3(128, 30, 128)
var c = Vector3(-128, 30, -128)
var d = Vector3(128, 0, -128)


func _ready():
#	var m_arr = generate_terrain()
#	self.mesh = made_mesh(m_arr)
#	self.mesh = made_mesh(update_terrain([]))
#	get_node("../StaticBody/CollisionShape").shape = self.mesh.create_trimesh_shape()
	
#	var kyk = self.mesh.get_faces()
	
	var arr = just_arr()
	print(arr.size(),'    ', arr[23].size())
	diamond_square(arr, a, b, c, d, 10)
	print(arr[0])
	self.mesh = made_mesh(generate_terrain(arr))
	self.set_surface_material(0, material)
	
	
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass
func just_arr():
	var result = []
	for i in range(257):
		var G = []
		for j in range(257):
			G.append([])
		result.append(G)
	result[0][0] = a
	result[256][0] = b
	result[0][256] = c
	result[256][256] = d
	return(result)





func generate_terrain(arr):
	var s = 0
	var result = PoolVector3Array()
	for i in range(100):
		for j in range(100):
			result.append(arr[i+1][j])
			result.append(arr[i][j+1])
			result.append(arr[i][j])
			result.append(arr[i+1][j+1])
			result.append(arr[i][j+1])
			result.append(arr[i+1][j])
	return(result)
	
	pass
func made_mesh(Arr):
	var mat = self.get_surface_material(0)
	var st = SurfaceTool.new()
	var tmpMesh = ArrayMesh.new()
	var arrays = Array()
	arrays.resize(ArrayMesh.ARRAY_MAX)
	arrays[ArrayMesh.ARRAY_VERTEX] = Arr
	
	
	
	var n_arr = PoolVector3Array()
	for i in range(Arr.size()/3):
		i *= 3
		var Dir = (Arr[i+1] - Arr[i]).cross(Arr[i+2] - Arr[i])
		var useless1 = Dir / Dir.length() * -1
		n_arr.append(useless1)
		n_arr.append(useless1)
		n_arr.append(useless1)
	arrays[ArrayMesh.ARRAY_NORMAL] = n_arr
	
	
	
	
	tmpMesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
	return(tmpMesh)

	
	
	
	
	
	
	
var a_1 = []
func update_terrain(Arr):
	var st = SurfaceTool.new()
	var result = []
	for i in range(100):
		result.append([])
		for j in range(100):
			result[i].append([])
	for l in range(100):
		result[0][l] = (Vector3(l, 0, 0))
		
		
	for k in range(1, 100, 1):
		var r = 0
		for m in range(100):
			if randf() > 0.66:
				r = 0.1
			else:
				r = -0.1
			result[k][m] = Vector3(result[k-1][m].x, result[k-1][m].y + r, result[k-1][m].z + 1)

	var mesharr = PoolVector3Array()
	for i in range(99):
		for j in range(99):
			mesharr.append(result[i][j])
			mesharr.append(result[i][j+1])
			mesharr.append(result[i+1][j])
			mesharr.append(result[i+1][j])
			mesharr.append(result[i][j+1])
			mesharr.append(result[i+1][j+1])
	return(mesharr)
	
	
	
	
func diamond_square(array, N, E, W, S, n):
#	print(n)
	n = 12
	var result = (N + E + W + S) / 4
#	for v in NEWS:
#		if typeof(v) == 7:
#			result += v
#		else:
#			if v == 0:
#				result.x -= NEWS[3].x
#				result.z -= NEWS[3].z
#			elif v == 3:
#				result.x -= NEWS[0].x
#				result.z -= NEWS[0].z
#			elif v == 1:
#				result.x -= NEWS[2].x
#				result.z -= NEWS[2].z
#			elif v == 2:
#				result.x -= NEWS[1].x
#				result.z -= NEWS[1].z
	result.y = result.y + rand_range(-1, 1) * (N - S).length() / n
	if int(result.x) != result.x:
#		n = 0
		return(0)
	array[result.x + 128][result.z + 128] = result
#	self.diamond_square(array, [result, NEWS[2] , NEWS[0] , 3])
#	self.diamond_square(array, [result, NEWS[0] , NEWS[1] , 3])
#	self.diamond_square(array, [result, NEWS[1] , NEWS[3] , 3])
#	self.diamond_square(array, [result, NEWS[3] , NEWS[2] , 3])
	var NW = Vector3()
	var NE = Vector3()
	var SW = Vector3()
	var SE = Vector3()
#	print(randf())
	NW.y = (result.y + N.y + W.y) / 3 + rand_range(-1, 1) * (N - W).length() / n
	NW.x = (N.x + W.x)/2
	NW.z = result.z
	array[NW.x + 128][NW.z + 128] = NW
	
	
	NE.y = (result.y + N.y + E.y) / 3 + rand_range(-1, 1) * (N - E).length() / n
	NE.z = (N.z + E.z)/2
	NE.x = result.x
	array[NE.x + 128][NE.z + 128] = NE
	
	SE.y = (result.y + S.y + E.y) / 3 + rand_range(-1, 1) * (S - E).length() / n
	SE.x = (S.x + E.x)/2
	SE.z = result.z
	array[SE.x + 128][SE.z + 128] = SE
	
	SW.y = (result.y + S.y + W.y) / 3 + rand_range(-1, 1) * (S - W).length() / n
	SW.z = (S.z + W.z)/2
	SW.x = result.x
	array[SW.x + 128][SW.z + 128] = SW
#	print(result.x, '     ', typeof(result.x))
	diamond_square(array, N, NE, NW, result, n)
	diamond_square(array, NE, E, result, SE, n)
	diamond_square(array, NW, result, W, SW, n)
	diamond_square(array, result, SE, SW, S, n)
#	n = 0