import json
import main

def decode_mission(dct):
	if "name" in dct:
		miss = main.mission(dct["name"], dct["reward"], dct["expectedduration"])
		if "cooldown" in dct:
			for i in dct["cooldown"]:
				miss.setcooldown(i, dct["cooldown"][i])
		return miss
	else:
		return dct

with open("missions.json") as missions_data:
	data = missions_data.read()
	missions = json.loads(data, object_hook=decode_mission)
