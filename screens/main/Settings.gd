extends Button

onready var timer = $HoldTimer

func _switch():
	get_tree().change_scene("res://screens/settings/settings.tscn")

func _on_HoldTimer_timeout():
	_switch()

func _on_Settings_button_down():
	timer.start()

func _on_Settings_button_up():
	timer.stop()
