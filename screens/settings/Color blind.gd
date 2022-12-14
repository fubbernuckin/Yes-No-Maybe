extends CheckBox

func _ready():
	pressed = Persist.get_color_blind()

func _on_Color_blind_toggled(button_pressed):
	Persist.set_color_blind(pressed)
