extends Spatial

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass
func move(direction):
	if direction == "right":
		for c in get_children():
			c.global_transform.origin.x -= 128
	elif direction == "left":
		for c in get_children():
			c.global_transform.origin.x += 128
	elif direction == "up":
		for c in get_children():
			c.global_transform.origin.z += 128
	elif direction == "down":
		for c in get_children():
			c.global_transform.origin.z -= 128
#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass
