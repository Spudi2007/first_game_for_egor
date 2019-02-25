extends KinematicBody

# class member variables go here, for example:
var a = 50
# var b = "textvar"

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass

func _process(delta):
#	print(self.global_transform.origin)
	if Input.is_action_pressed("ui_up"):
		self.move_and_slide(Vector3(a,0,0))
	elif Input.is_action_pressed("ui_down"):
		self.move_and_slide(Vector3(-a,0,0))
	if Input.is_action_pressed("ui_left"):
		self.move_and_slide(Vector3(0,0,a))
	elif Input.is_action_pressed("ui_right"):
		self.move_and_slide(Vector3(0,0,-a))
	if Input.is_action_pressed("q"):
		get_node("Position3D").rotate_y(-delta)
	elif Input.is_action_pressed("e"):
		get_node("Position3D").rotate_y(delta)
	if Input.is_action_pressed("space"):
		self.move_and_slide(Vector3(0,a,0))
	elif Input.is_action_pressed("shift"):
		self.move_and_slide(Vector3(0,-a,0))