import main

def decode_mission(dict_):
	if "name" in dict_:
		miss = main.Mission(dict_["name"], dict_["reward"], dict_["expectedduration"])
		if "cooldown" in dict_:
			for i in dict_["cooldown"]:
				miss.cooldowntimes[i] = dict_["cooldown"][i]
		else:
			del miss.cooldowntimes
		if "group" in dict_:
			miss.group = dict_["group"]
		if "tax" in dict_:
			miss.tax = dict_["tax"]
		if "required" in dict_:
			miss.required = dict_["required"]
		return miss
	else:
		return dict_

def decode_player(dict_):
    if "name" in dict_:
        ply = main.Player(dict_["name"], dict_["business"])
    return ply

def get_mpt(mission):
	return (mission.reward - mission.tax)/mission.expectedduration
