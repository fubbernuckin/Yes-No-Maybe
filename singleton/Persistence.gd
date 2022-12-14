extends Node

var settings_dict = {
	"press_mode":0, #0=press, 1=double press, 2 = long press
	"color_blind":false,
	"flash":true,  #makes other buttons change grey
	"sound":true  #plays sound when buttons are pressed
}

func _ready():
	file_load()

func set_flash(param:bool):
	settings_dict["flash"] = param
	file_save()
func get_flash():
	return settings_dict.get("flash")

func set_color_blind(param:bool):
	settings_dict["color_blind"] = param
	file_save()
func get_color_blind():
	return settings_dict.get("color_blind")

func set_sound(param:bool):
	settings_dict["sound"] = param
	file_save()
func get_sound():
	return settings_dict.get("sound")

func set_press_mode(param:int):
	settings_dict["press_mode"] = param
	file_save()
func get_press_mode():
	return settings_dict.get("press_mode")

func file_save():
	var file = File.new()
	file.open("user://settings.json", File.WRITE)
	file.store_line(to_json(settings_dict))

func file_load():
	var file = File.new()
	if not file.file_exists("user://settings.json"):
		file_save()
		return
	file.open("user://settings.json", File.READ)
	var data = parse_json(file.get_as_text())
	settings_dict = data
