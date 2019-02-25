extends MeshInstance

# class member variables go here, for example:
var M = ArrayMesh.new()
var material = self.get_surface_material(0)
var arr = Array()

var thread = Thread.new()
var thread_queue = [[3,4],[4,4],[5,4],[3,5],[4,5],[5,5]]
var big_map_move_queue = []


var points = [Vector3(64, 64, 64)]
var one_square_size = 32 # *4

var map_current_location = Vector2(0,0)
var big_map_location = Vector2(0,0)
var map_size = 11 # this for archive points only REAL MAP SIZE = THIS - 2
var map = []



func _ready():
	for i in range(map_size):
		var u = []
		for j in range(map_size):
			var u2 = Array()
			u.append(u2)
		map.append(u)
	pass

func _process(delta):
	if Input.is_action_just_pressed('2'):
		center_of_map_move("left")
		
	if Input.is_action_just_pressed('3'):
		center_of_map_move("up")
		
	if Input.is_action_just_pressed('1'):
		center_of_map_move("right")
	if Input.is_action_just_pressed('4'):
		center_of_map_move("down")
			
	if thread_queue and !thread.is_active():
		thread.start(self, "d_s_gen", [32, thread_queue[0][0], thread_queue[0][1]])
		thread_queue.pop_front()
	if big_map_move_queue and !thread_queue and !thread.is_active():
		center_of_map_move(big_map_move_queue[0])
		big_map_move_queue.pop_front()
		
		
		
	# MOVING_BIG_MAP
	if (abs(get_node("../Player").global_transform.origin.x - big_map_location.x) >= 256 - 64) or (abs(get_node("../Player").global_transform.origin.z - big_map_location.y) >= 256-64):

		if abs(get_node("../Player").global_transform.origin.x - big_map_location.x) >= 256 - 64:
			if get_node("../Player").global_transform.origin.x - big_map_location.x > 0:
				big_map_move_queue.append("right")
				big_map_location.x += 128
			elif get_node("../Player").global_transform.origin.x - big_map_location.x < 0:
				big_map_move_queue.append("left")
				big_map_location.x -= 128
		elif abs(get_node("../Player").global_transform.origin.z - big_map_location.y) >= 256-64:
			if get_node("../Player").global_transform.origin.z - big_map_location.y > 0:
				big_map_move_queue.append("down")
				big_map_location.y += 128
			elif get_node("../Player").global_transform.origin.z - big_map_location.y < 0:
				big_map_move_queue.append("up")
				big_map_location.y -= 128
		
		
		
		
		
		
		
		
#SQuAD_BASED GENERATION
	if (abs(get_node("../Player").global_transform.origin.x - map_current_location.x) >= 128/2) or (abs(get_node("../Player").global_transform.origin.z - map_current_location.y) >= 128/2):

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
		
		

# NEED TO MADE THIS FUNC !!!!
func center_of_map_move(direction):
	
	
	
	if direction == "right":
		get_node("../map").get_child(0).global_transform.origin.x += 128 * 9
		get_node("../Col_map").get_child(0).global_transform.origin.x += 128 * 9
		for i in range(map_size-2):
#			get_node("../map").get_child(0).get_child(i).global_transform.origin.x += 128 * 9
			if get_node("../map").get_child(0).get_child(i).mesh:
				get_node("../map").get_child(0).get_child(i).mesh = null
			if get_node("../Col_map").get_child(0).get_child(i).shape:
				get_node("../Col_map").get_child(0).get_child(i).shape = null
		get_node("../map").move_child(get_node("../map").get_child(0), 8)
		get_node("../Col_map").move_child(get_node("../Col_map").get_child(0), 8)
		for i in range(map_size-1):
			print(i)
			map[i] = map[i+1]
		map[map_size-1] = [[],[],[],[],[],[],[],[],[],[],[]]
		map_current_location.x -= 128
		big_map_location.x -= 128
		
		
	elif direction == "down":
#		get_node("../map").get_child(0).global_transform.origin.x += 128 * 9
		for i in range(map_size-2):
			get_node("../map").get_child(i).get_child(0).global_transform.origin.z += 128 * 9
			get_node("../Col_map").get_child(i).get_child(0).global_transform.origin.z += 128 * 9
			
			if get_node("../map").get_child(i).get_child(0).mesh:
				get_node("../map").get_child(i).get_child(0).mesh = null
			get_node("../map").get_child(i).move_child(get_node("../map").get_child(i).get_child(0), 8)
			get_node("../Col_map").get_child(i).move_child(get_node("../Col_map").get_child(i).get_child(0), 8)
		for i in range(map_size):
			for j in range(map_size-1):
				map[i][j] = map[i][j+1]
			map[i][map_size-1] = []
		map_current_location.y -= 128
		big_map_location.y -= 128
		


	elif direction == "left":
		get_node("../map").get_child(map_size-3).global_transform.origin.x -= 128 * 9
		get_node("../Col_map").get_child(map_size-3).global_transform.origin.x -= 128 * 9
		for i in range(map_size-2):
#			get_node("../map").get_child(map_size-3).get_child(i).global_transform.origin.x -= 128 * 9
			if get_node("../map").get_child(map_size-3).get_child(i).mesh:
				get_node("../map").get_child(map_size-3).get_child(i).mesh = null

		get_node("../map").move_child(get_node("../map").get_child(map_size-3), 0)
		get_node("../Col_map").move_child(get_node("../Col_map").get_child(map_size-3), 0)
		for i in range(map_size-1, 0, -1):
			map[i] = map[i-1]
		map[0] = [[],[],[],[],[],[],[],[],[],[],[]]
		map_current_location.x += 128
		big_map_location.x += 128

	elif direction == "up":
#		get_node("../map").get_child(map_size-3).global_transform.origin.x -= 128 * 9
		for i in range(map_size-2):
			get_node("../map").get_child(i).get_child(map_size-3).global_transform.origin.z -= 128 * 9
			get_node("../Col_map").get_child(i).get_child(map_size-3).global_transform.origin.z -= 128 * 9
			if get_node("../map").get_child(i).get_child(map_size-3).mesh:
				get_node("../map").get_child(i).get_child(map_size-3).mesh = null
			get_node("../map").get_child(i).move_child(get_node("../map").get_child(i).get_child(map_size-3), 0)
			get_node("../Col_map").get_child(i).move_child(get_node("../Col_map").get_child(i).get_child(map_size-3), 0)
		for i in range(map_size):
			for j in range(map_size-1, 0, -1):
				map[i][j] = map[i][j-1]
			map[i][0] = []
		map_current_location.y += 128
		big_map_location.y += 128

	get_parent().move(direction)



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
	args[2] += 1
	args[1] += 1
	var tmpMesh
	var array = []
	var step = 1
	var pos = [args[1], args[2]]
	var points = map[args[1]][args[2]]
	
#	if points:
#		print(points)
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
		square(array, step, 0.2, size)
		diamond(array, step, 0.2, size)
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
			
			
			

	tmpMesh = made_mesh(array)
	var mat = material
	get_node("../Col_map").get_child(args[1]-1).get_child(args[2]-1).shape = tmpMesh.create_trimesh_shape()
	tmpMesh.surface_set_material(0, material)
	
	call_deferred("load_done")

	return([tmpMesh, args[1], args[2], mat])
	
func load_done():
	var a = thread.wait_to_finish()
	get_node("../map").get_child(a[1]-1).get_child(a[2]-1).mesh = a[0]
#	get_node("../map").get_child(a[1]-1).get_child(a[2]-1).set_surface_material(0, a[3])

	
	
	
func do_all():
	if (thread.is_active()):
		return
	thread.start(self, "d_s_gen", 64)