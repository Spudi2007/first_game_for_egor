extends MeshInstance

# class member variables go here, for example:
var M = ArrayMesh.new()
var material = self.get_surface_material(0)
var arr = Array()

var thread = Thread.new()
var thread_queue = []

var points = [Vector3(64, 64, 64)]
var one_square_size = 32 # *4

var map_current_location = Vector2(0,0)
var map_size = 11 # this for archive points only REAL MAP SIZE = THIS - 2
var map = []





func _ready():
	for i in range(map_size):
		var u = []
		for j in range(map_size):
			var u2 = Array()
			u.append(u2)
		map.append(u)
#	for i in range(129):
#		map[2][2].append(Vector3(i, 0, 0))
#		map[2][2].append(Vector3(0, 0, i))
#		map[2][2].append(Vector3(i, 0, 128))
#		map[2][2].append(Vector3(128, 0, i))
#		points.append([i, 0, Vector3(i, 0, 0)])
#	points = map[1][1]
#	map[2][2] = (Vector3(64,64,64))
	pass

func _process(delta):
	if Input.is_action_just_pressed('2'):
		thread_queue.append([8, 8])
		
	if Input.is_action_just_pressed('3'):
		thread_queue.append([2, 3])
		
	if Input.is_action_just_pressed('1'):
		center_of_map_move("right")
			
	if thread_queue and !thread.is_active():
		thread.start(self, "d_s_gen", [32, thread_queue[0][0], thread_queue[0][1]])
		thread_queue.pop_front()
#SQuAD_BASED GENERATION
	if (abs(get_node("../Player").global_transform.origin.x - map_current_location.x) >= 128/2) or (abs(get_node("../Player").global_transform.origin.z - map_current_location.y) >= 128/2):
#		for i in range(5):
#			for j in range(5):
#				if !get_node("../map").get_child((map_current_location.x/128) + i + 2).get_child(map_current_location.y/128 + j + 2).mesh:
#					thread_queue.append([(map_current_location.x/128) + i + 2, map_current_location.y/128 + j + 2])
					
		
		if abs(get_node("../Player").global_transform.origin.x - map_current_location.x) >= 128/2:
			if get_node("../Player").global_transform.origin.x - map_current_location.x > 0:
				map_current_location.x += 128
			elif get_node("../Player").global_transform.origin.x - map_current_location.x < 0:
				map_current_location.x -= 128
			print(map_current_location)
		elif abs(get_node("../Player").global_transform.origin.z - map_current_location.y) >= 128/2:
			if get_node("../Player").global_transform.origin.z - map_current_location.y > 0:
				map_current_location.y += 128
			elif get_node("../Player").global_transform.origin.z - map_current_location.y < 0:
				map_current_location.y -= 128
			print(map_current_location)
			
		
		for i in range(5):
			for j in range(5):
				if !get_node("../map").get_child((map_current_location.x/128) + i + 2).get_child(map_current_location.y/128 + j + 2).mesh:
					thread_queue.append([(map_current_location.x/128) + i + 2, map_current_location.y/128 + j + 2])
		
		
#	if abs(get_node("../Player").global_transform.origin.x - map_current_location.x) >= 128/2:
##		print('pinis')
#		if get_node("../Player").global_transform.origin.x - map_current_location.x > 0:
#			if (thread.is_active()):
#				print("YYYY SUKAA")
#			else:
#				print((map_current_location.x/128) + 1 + 3, map_current_location.y/128 + 2)
##				thread.start(self, "d_s_gen", [32, (map_current_location.x/128) + 1 + 2, map_current_location.y/128 + 2])
#				if !get_node("../map").get_child((map_current_location.x/128) + 1 + 2).get_child(map_current_location.y/128 + 2).mesh:
#					thread_queue.append([(map_current_location.x/128) + 1 + 2, map_current_location.y/128 + 2])
#				if !get_node("../map").get_child((map_current_location.x/128) + 1 + 2).get_child(map_current_location.y/128 + 2+1).mesh:
#					thread_queue.append([(map_current_location.x/128) + 1 + 2, map_current_location.y/128 + 2 + 1])
#				if !get_node("../map").get_child((map_current_location.x/128) + 1 + 2).get_child(map_current_location.y/128 + 2-1).mesh:
#					thread_queue.append([(map_current_location.x/128) + 1 + 2, map_current_location.y/128 + 2 - 1])
##				map_current_location.x += 128
#		else:
#			if (thread.is_active()):
#				print("YYYY SUKAA")
#			else:
#				print((map_current_location.x/128) - 1 + 3, map_current_location.y/128 + 2)
#				thread.start(self, "d_s_gen", [32, (map_current_location.x/128) - 1 + 2, map_current_location.y/128 + 2])
#				map_current_location.x -= 128
#		pass
#	elif abs(get_node("../Player").global_transform.origin.z - map_current_location.y) >= 129/2:
#		pass
		

# NEED TO MADE THIS FUNC !!!!
func center_of_map_move(direction):
	if direction == "right":
#		for i in range(map_size-3):
#			for j in range(map_size-2):
#				get_node("../map").get_child(i).get_child(j).global_transform.origin.x += 128
		for i in range(map_size-2):
			get_node("../map").get_child(0).get_child(i).global_transform.origin.x += 128 * 9
			if get_node("../map").get_child(0).get_child(i).mesh:
				get_node("../map").get_child(0).get_child(i).mesh = null
		
		get_node("../map").move_child(get_node("../map").get_child(0), 8)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#	if direction == "right":
#		for i in range(map_size - 1):
#			for j in range(map_size):
#				map[i][j] = map[i+1][j]
#		for i in range(map_size):
#			map[6][i] = []
#	if direction == "left":
#		for i in range(map_size - 1):
#			for j in range(map_size):
#				map[map_size - i][j] = map[map_size - (i+1)][j]
#		for i in range(map_size):
#			map[0][i] = []
#	if direction == "up":
#		for i in range(map_size):
#			for j in range(map_size - 1):
#				map[i][j] = map[i+1][j]
#		for i in range(map_size):
#			map[6][i] = []
#	if direction == "down":
#		for i in range(map_size):
#			for j in range(map_size - 1):
#				map[i][j] = map[i+1][j]
#		for i in range(map_size):
#			map[6][i] = []
	
	


func made_mesh(arr):
	var s = 0
	var result = PoolVector3Array()
	var tmpMesh = ArrayMesh.new()
	var arrays = Array()
	for i in range(arr.size()-1):
		for j in range(arr.size()-1):
			result.append(arr[i+1][j] - Vector3(arr.size() - 1, 0, arr.size() - 1)/2)
			result.append(arr[i][j+1]- Vector3(arr.size() - 1, 0, arr.size() - 1)/2)
			result.append(arr[i][j]- Vector3(arr.size() - 1, 0, arr.size() - 1)/2)
			result.append(arr[i+1][j+1]- Vector3(arr.size() - 1, 0, arr.size() - 1)/2)
			result.append(arr[i][j+1]- Vector3(arr.size() - 1, 0, arr.size() - 1)/2)
			result.append(arr[i+1][j]- Vector3(arr.size() - 1, 0, arr.size() - 1)/2)

	arrays.resize(ArrayMesh.ARRAY_MAX)
	arrays[ArrayMesh.ARRAY_VERTEX] = result


# 	NORMALS
	var n_arr = PoolVector3Array()
	for i in range(result.size()/3):
		i *= 3
		var Dir = (result[i+1] - result[i]).cross(result[i+2] - result[i])
		var useless1 = Dir / Dir.length() * -1
		n_arr.append(useless1)
		n_arr.append(useless1)
		n_arr.append(useless1)
	arrays[ArrayMesh.ARRAY_NORMAL] = n_arr




	tmpMesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
	return(tmpMesh)




func square(arr, step,r, size):
	step -= 1
	var k = step
	step = 1
	if k != 0:
		for i in range(k):
			step *= 2
	else:
		pass
	var dist = size / step
	
	for i in range(step):
		for j in range(step):
			var NW = arr[i*dist][j*dist]
			var NE = arr[i*dist+dist][j*dist]
			var SE = arr[i*dist+dist][j*dist+dist]
			var SW = arr[i*dist][j*dist+dist]
			var C = (NW + NE + SE + SW) / 4
			C.y += rand_range(-r * dist, r * dist)
			if arr[C.x][C.z] == []:
				arr[C.x][C.z] = C
	return(arr)
			
func diamond(arr, step, r, size):
	var k = step
	var step_hor = 1
	var step_vert = 1
	for i in range(k):
		step_hor *= 2
	var dist = size/step_hor
	step_hor += 1
	for i in range(k-1):
		step_vert *= 2
	step_vert += 1
	for i in range(step_hor):
		for j in range(step_vert):
			var C = Vector3(0,0,0)
			if i % 2 == 0:
				C.z += dist
			else:
				pass
			C.z += j * dist * 2
			C.x += i * dist
			if (C.x >= 0) and (C.z >= 0) and (C.x <= size) and (C.z <= size):
				var n = 0 
				if C.z - dist >= 0:
					n += 1
					C.y += arr[C.x][C.z - dist].y
				if C.z + dist <= size:
					n += 1
					C.y += arr[C.x][C.z + dist].y
				if C.x - dist >= 0:
					n += 1
					C.y += arr[C.x - dist][C.z].y
				if C.x + dist <= size:
					n += 1
					C.y += arr[C.x + dist][C.z].y
				C.y /= n
				C.y += rand_range(-r * dist * 1.42, r * dist * 1.42)
				if typeof(arr[C.x][C.z]) != 7:
					arr[C.x][C.z] = C
	return(arr)



func d_s_gen(args):
	var size = args[0]*4
	var tmpMesh
	var array = []
	var step = 1
	var pos = [args[1], args[2]]
	var points = map[args[1]][args[2]]
#	get_node("../map").get_child(args[1]).get_child(args[2]).points
#	map[args[1]][args[2]]

	for i in range(size+1):
		var u = []
		for j in range(size+1):
			u.append([])
		array.append(u)
	array[0][0] = Vector3(0, rand_range(-size/4, size/4), 0)
	array[size][0] = Vector3(size, rand_range(-size/4, size/4), 0)
	array[0][size] = Vector3(0, rand_range(-size/4, size/4), size)
	array[size][size] = Vector3(size, rand_range(-size/4, size/4), size)
	
#GEttING POINTS FROM MAP
	for i in range(points.size()):
		array[points[i].x][points[i].z] = points[i]
		
#	print(array)
#
#
#	print(args)
	for i in range(7):
		square(array, step, 0.15, size)
		diamond(array, step, 0.15, size)
		step += 1
	
	
#ADDING POINTS TO MAP

	print('start', args)
	for i in range(array.size()):
		if array[i][size] in map[args[1]][args[2]+1]:
			pass
		else:
			map[args[1]][args[2]+1].append(array[i][size] - Vector3(0,0,128))
		if array[i][0] in map[args[1]][args[2]-1]:
			pass
		else:
			map[args[1]][args[2]-1].append(array[i][0] + Vector3(0,0,128))
		if array[size][i] in map[args[1]+1][args[2]]:
			pass
		else:
			map[args[1]+1][args[2]].append(array[size][i] - Vector3(128,0,0))
		if array[0][i] in map[args[1]-1][args[2]]:
			pass
		else:
			map[args[1]-1][args[2]].append(array[0][i] + Vector3(128,0,0))
	print('end')
	
#	print('start')
#	for i in range(array.size()):
#		if !(array[i][size] in get_node("../map").get_child(args[1]).get_child(args[2]+1).points):
#			get_node("../map").get_child(args[1]).get_child(args[2]+1).points.append(array[i][size] - Vector3(0,0,128))
##		else:
##			map[args[1]][args[2]+1].append(array[i][size] - Vector3(0,0,128))
#		if !(array[i][0] in get_node("../map").get_child(args[1]).get_child(args[2]-1).points):
#			get_node("../map").get_child(args[1]).get_child(args[2]-1).points.append(array[i][0] + Vector3(0,0,128))
##		else:
##			map[args[1]][args[2]-1].append(array[i][0] + Vector3(0,0,128))
#		if !(array[size][i] in get_node("../map").get_child(args[1]+1).get_child(args[2]).points):
#			get_node("../map").get_child(args[1]+1).get_child(args[2]).points.append(array[size][i] - Vector3(128,0,0))
##		else:
##			map[args[1]+1][args[2]].append(array[size][i] - Vector3(128,0,0))
#		if !(array[0][i] in get_node("../map").get_child(args[1]-1).get_child(args[2]).points):
#			get_node("../map").get_child(args[1]-1).get_child(args[2]).points.append(array[0][i] + Vector3(128,0,0))
##		else:
##			map[args[1]-1][args[2]].append(array[0][i] + Vector3(128,0,0))
#	print('end')
	tmpMesh = made_mesh(array)
	var mat = material
#	get_node("../Col_map/CollisionShape").shape = tmpMesh.create_trimesh_shape()
#	get_node("../map").get_child(args[1]).get_child(args[2]).set_surface_material(0, material)
#	get_node("../StaticBody/CollisionShape").shape = tmpMesh.create_trimesh_shape()
	
	call_deferred("load_done")

	return([tmpMesh, args[1], args[2], mat])
	
func load_done():
	var a = thread.wait_to_finish()
	get_node("../map").get_child(a[1]).get_child(a[2]).mesh = a[0]
	get_node("../map").get_child(a[1]).get_child(a[2]).set_surface_material(0, a[3])
#	get_node("../StaticBody/CollisionShape").shape = a.create_trimesh_shape()
#	get_child(0).global_transform.origin = Vector3(100,0,100)

	
	
	
func do_all():
	if (thread.is_active()):
		return
	thread.start(self, "d_s_gen", 64)