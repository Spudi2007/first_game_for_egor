extends KinematicBody

var g = Vector3(0, -20, 0)
var speed = 10


var current_speed = Vector3()
var current_speed_buffer = Vector3()
var n = 0

var V = Vector3()
var space_state = null
var down_speed = Vector3()
var pounce = 0
var right = Vector3()
var forward = Vector3()

var anim_tree
var status = "in_flight"
var camera
var rotation_helper

var MOUSE_SENSITIVITY = 0.1



func _ready():
	camera = get_node("Rot_helper/camera_position")
	rotation_helper = get_node("Rot_helper")
	anim_tree = get_node("Mesh_rot_helper/Mesh").get_node("AnimationTree")
	
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
#	set_process(true)
	pass

func _process(delta):
	n += delta
	if pounce > 0:
		pounce -= delta
	if current_speed_buffer != self.global_transform.origin:
		current_speed = (self.global_transform.origin - current_speed_buffer) / delta
		current_speed_buffer = self.global_transform.origin
		n = 0
		
	V = Vector3(0,0,0)
	right = get_node("Rot_helper/right").global_transform.origin - self.global_transform.origin
	forward = get_node("Rot_helper/forward").global_transform.origin - self.global_transform.origin
	if Input.is_action_pressed("move_forward"):
		V += forward * speed
	if Input.is_action_pressed("move_backward"):
		V -= forward * speed
	if Input.is_action_pressed("move_left"):
		V -= right * speed
	if Input.is_action_pressed("move_right"):
		V += right * speed
		
	if Input.is_action_pressed("shift"):
		V *= 3
	if Input.is_action_just_pressed("ui_accept"):
		down_speed += Vector3(0, 20, 0)
		pounce = 1
#		get_node("Mesh_rot_helper/Mesh").get_node("AnimationTreePlayer").oneshot_node_start("jump")


	
	space_state = get_world().direct_space_state
	var result = space_state.intersect_ray(self.global_transform.origin, self.global_transform.origin + Vector3(0,-3.1,0), [self])
	down_speed += g * delta
	if result and pounce < 0:
		self.global_transform.origin = result["position"] + Vector3(0, 3, 0)
#		print(result)
		if result["normal"].y > 0.8:
			status = "on_floor"
#			get_node("Mesh_rot_helper/Mesh").get_node("AnimationTreePlayer").blend2_node_set_amount("jump", .0)
			down_speed = Vector3(0,0,0)
	else:
		status = "in_flight"
	V += down_speed
	move_and_slide(V)
	
	
	
	# ANIME
	
	if (pounce == 1) or (status == "in_flight" and !get_node("Mesh_rot_helper/Mesh").get_node("AnimationTree")["parameters/jump/active"] and down_speed.y < -10):
		anim_tree["parameters/jump/active"] = true
	elif status == "on_floor" and get_node("Mesh_rot_helper/Mesh").get_node("AnimationTree")["parameters/jump/active"]:
		anim_tree["parameters/jump/active"] = false
#

	
#	var u = Vector3(current_speed.x, 0, current_speed.z).cross(Vector3(1,0,0))
#	get_node("Mesh_rot_helper").rotation.y = Vector3(current_speed.x, 0, current_speed.z).angle_to(Vector3(1,0,0)) * -sign(u.y)
	if Vector3(current_speed.x, 0, current_speed.z).length() > 1:
		var u = Vector3(current_speed.x, 0, current_speed.z).cross(Vector3(1,0,0))
		get_node("Mesh_rot_helper").rotation.y = Vector3(current_speed.x, 0, current_speed.z).angle_to(Vector3(1,0,0)) * -sign(u.y)
#		print(Vector3(current_speed.x, 0, current_speed.z).length())
		anim_tree["parameters/run/blend_amount"] = 1
	else:
		anim_tree["parameters/run/blend_amount"] = 0


func _input(event):
	if event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		rotation_helper.rotate((get_node("Rot_helper/right").global_transform.origin - self.global_transform.origin).normalized(), deg2rad(event.relative.y * MOUSE_SENSITIVITY * -1))
		rotation_helper.rotate_y(deg2rad(event.relative.x * MOUSE_SENSITIVITY * -1))
#		get_node("Mesh_rot_helper").rotate_y(deg2rad(event.relative.x * MOUSE_SENSITIVITY * -1))
#        var camera_rot = rotation_helper.rotation_degrees
#        camera_rot.x = clamp(camera_rot.x, -70, 70)
#        rotation_helper.rotation_degrees = camera_rot