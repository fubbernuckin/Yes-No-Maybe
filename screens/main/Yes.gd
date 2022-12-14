extends Button

var style = preload("res://style boxes/Yes.tres")
var stylecb = preload("res://style boxes/Color_Blind_Yes.tres")
var grey = preload("res://style boxes/Grey.tres")
var flash = Persist.get_flash()
onready var audio = $AudioStreamPlayer

func _ready():
	set_normal()

func set_grey():
	add_stylebox_override("normal", grey)
	add_stylebox_override("hover", grey)

func set_normal():
	if (Persist.get_color_blind()):
		add_stylebox_override("normal", stylecb)
		add_stylebox_override("hover", stylecb)
	else:
		add_stylebox_override("normal", style)
		add_stylebox_override("hover", style)



func _on_ClickTimer_timeout():
	set_normal()

func _on_Maybe_button_up():
	if (flash):
		set_grey()

func _on_No_button_up():
	if (flash):
		set_grey()

func _on_Yes_button_up():
	set_normal()
	audio.play()
