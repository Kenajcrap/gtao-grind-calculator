from time import time, sleep

class Mission:

	def __init__(self, name, reward, expectedduration):
		self.name = name
		self.group = ""
		self.cooldowntimes = {}
		self.reward = reward
		self.tax = 0
		self.expectedduration = expectedduration
		self.required = []

	def _getcooldown(self):
		try:
			return max(0, self._cooldownend - time())
		except AttributeError:
			return 0

	def _setcooldown(self, seconds):
		self._cooldownend = time() + seconds

	cooldown  = property(_getcooldown, _setcooldown)

	def startcooldown(self, event):
		try:
			self._cooldownend = time() + self.cooldowntimes[event]
		except AttributeError:
			self._cooldownend = time()

class SupplyMission(Mission):

	pass

class DeliveryMission(Mission):
	
	pass

class Player():
	
	def __init__(self, name, business):
		self.name = name
		self.business = business