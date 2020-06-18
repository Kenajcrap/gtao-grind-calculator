import json
import util
from threading import Thread

class Calculator():

	def __init__(self):
		with open("player.json") as player_data:
			self.ply = json.loads(player_data.read(), object_hook=util.decode_player)
			
		with open("missions.json") as missions_data:
			self.missions = json.loads(missions_data.read(), object_hook=util.decode_mission)
		
		self.missions.sort(reverse=True, key=util.get_mpt)
	
	def set_finished(self, mission):
		mission.startcooldown("onfinish")
		if mission.group != "":
			for miss in self.missions:
				if (miss.group == mission.group) and (miss.name != mission.name):
					miss.startcooldown("ongroupfinish")
	
	def get_first_available(self):
		for miss in self.missions:
			if (miss.cooldown == 0) and all(elem in self.ply.business for elem in miss.required):
				return miss
				
calc = Calculator()

answer = ""
while answer != "exit":
	calc.missions.sort(reverse=True, key=util.get_mpt)
	for i in calc.missions:
		print("{} -- {}".format(i.name, i.cooldown))
	
	print("currently the best avaliable mission is {}".format(calc.get_first_available().name))
	answer = input("any key to finish mission, 'exit' to stop")
	calc.set_finished(calc.get_first_available())