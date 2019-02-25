extends Spatial

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	for i in range(9):
		get_child(i).global_transform.origin.x = 128 * (i-4)
		for j in range(9):
			get_child(i).get_child(j).global_transform.origin.z = 128 * (j-4)
			
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass
