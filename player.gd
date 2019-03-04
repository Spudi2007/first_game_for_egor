extends KinematicBody

var g = Vector3(0, -20, 0)
var speed = 10
var V = Vector3()
var space_state = null
var down_speed = Vector3()

var right = Vector3()
var forward = Vector3()


var camera
var rotation_helper

var MOUSE_SENSITIVITY = 0.1


func _ready():
	camera = get_node("Rot_helper/camera_position")
	rotation_helper = get_node("Rot_helper")

	
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
#	set_process(true)
	pass

func _process(delta):
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
	
	space_state = get_world().direct_space_state
	var result = space_state.intersect_ray(self.global_transform.origin, self.global_transform.origin + Vector3(0,-3,0), [self])
	down_speed += g * delta
	if result:
		self.global_transform.origin = result["position"] + Vector3(0, 3, 0)
#		print(result)
		if result["normal"].y > 0.8:
			down_speed = Vector3(0,0,0)
#
	V += down_speed
	move_and_slide(V)
	pass

func _input(event):
    if event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
        rotation_helper.rotate((get_node("Rot_helper/right").global_transform.origin - self.global_transform.origin).normalized(), deg2rad(event.relative.y * MOUSE_SENSITIVITY * -1))
        rotation_helper.rotate_y(deg2rad(event.relative.x * MOUSE_SENSITIVITY * -1))

#        var camera_rot = rotation_helper.rotation_degrees
#        camera_rot.x = clamp(camera_rot.x, -70, 70)
#        rotation_helper.rotation_degrees = camera_rot