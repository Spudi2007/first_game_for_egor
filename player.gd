extends KinematicBody

var g = Vector3(0, -10, 0)
var speed = 10
var V = Vector3()
var space_state = null
var d = Vector3()


func _ready():
	set_process(true)
	pass

func _process(delta):
	V = Vector3(0,0,0)
	if Input.is_action_pressed("ui_up"):
		V += (get_node("MeshInstance/forward").global_transform.origin - self.global_transform.origin) * speed
	if Input.is_action_pressed("ui_down"):
		V -= (get_node("MeshInstance/forward").global_transform.origin - self.global_transform.origin) * speed
	if Input.is_action_pressed("ui_left"):
		V -= (get_node("MeshInstance/right").global_transform.origin - self.global_transform.origin) * speed
	if Input.is_action_pressed("ui_right"):
		V += (get_node("MeshInstance/right").global_transform.origin - self.global_transform.origin) * speed
	if Input.is_action_pressed("e"):
		get_node("MeshInstance").rotate_y(delta)
		get_node("Position3D2").rotate_y(delta)
	if Input.is_action_pressed("q"):
		get_node("MeshInstance").rotate_y(-delta)
		get_node("Position3D2").rotate_y(-delta)
	
	space_state = get_world().direct_space_state
	var result = space_state.intersect_ray(self.global_transform.origin, self.global_transform.origin + Vector3(0,-2,0), [self])
	d += g * delta
	if result:
#		print(result)
		if result["normal"].y > 0.8:
			d = Vector3(0,0,0)
#
	V += d
	move_and_slide(V)
	pass

#func _integrate_forces(state):
#	if V.length() > 0:
#		state.linear_velocity += V
#	state.add_force(V,Vector3(0,0,0))