extends AudioStreamPlayer

# class member variables go here, for example:
var u = 0
# var b = "textvar"

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass

func _process(delta):
	if int(self.get_playback_position() * 10) == 50:
		self.play(1.62)
#		u += 0.1
		
#	pass
