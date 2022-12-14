extends CheckBox

func _ready():
	pressed = Persist.get_flash()

func _on_Flash_toggled(button_pressed):
	Persist.set_flash(pressed)
