from time import time, sleep

class mission:

	def __init__(self, name, reward, expectedduration):
		self.name = name
		self.reward = reward
		self.expectedduration = expectedduration

	def setcooldowntime(self, event, seconds):
		try:
			self.cooldowntimes[event] = seconds
		except AttributeError:
			self.cooldowntimes = {}
			self.cooldowntimes[event] = seconds
	
	def _startcooldown(self, event):
		try:
			self.cooldownend = time() + self.cooldownontimes[event]
		except AttributeError:
			raise AttributeError("Mission has no cooldown times set, set it with setcooldowntime(String event, Int seconds)")

	def _getcooldown(self):
		try:
			return max(0, self.cooldownend - time())
		except AttributeError:
			return 0
	
	def _setcooldown(self, seconds):
		self.cooldownend = time() + seconds

	cooldown  = property(_getcooldown, _setcooldown)

	def finish(self):
		try:
			self._startcooldown("onfinish")
		except AttributeError:
			raise AttributeError("Tried to trigger before setcooldowntime('onfinish', seconds)")

	def trigger(self):
		try:
			self._startcooldown("ontrigger")
		except AttributeError:
			raise AttributeError("Tried to trigger() before setcooldowntime('ontrigger', seconds)")

	def clear(self):
		self.cooldown = 0



class supplymission(mission):

	pass

class deliverymission(mission):
	
	pass