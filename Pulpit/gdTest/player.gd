extends Sprite

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
var mousepos = 0

func _ready():
	# Called every time the node is added to the scene.
	# Initialization here
	set_process(true)

func _process(delta):
	mousepos = get_global_mouse_pos()
	look_at(mousepos)