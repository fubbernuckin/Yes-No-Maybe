extends CheckBox

func _ready():
	if (Persist.get_press_mode() == 2):
		pressed = true
	else:
		pressed = false

func _on_Double_click_pressed():
	pressed = false

func _on_Long_press_pressed():
	if (pressed):
		Persist.set_press_mode(2)
	else:
		Persist.set_press_mode(0)
