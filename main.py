from time import time, sleep

class mission:

	def __init__(self, name, reward, expectedduration):
		self.name = name
		self.reward = reward
		self.expectedduration = expectedduration
		self.cooldownend = 0
	
	def getname(self):
		return self.name

	def setcooldown(self, event, seconds):
		if event == "ontrigger":
			self.cooldownontrigger = seconds
		elif event == "onfinish":
			self.cooldownonfinish = seconds
	
	def startcooldown(self, event):
		if event == "ontrigger":
			self.cooldownend = time() + self.cooldownontrigger
		elif event == "onfinish":
			self.cooldownend = time() + self.cooldownonfinish
	
	def getcooldown(self):
		return max(0, self.cooldownend-time())

	def finish(self):
		try:
			self.startcooldown("onfinish")
		except AttributeError:
			raise Exception("Tried to trigger before setcooldown('finish', seconds)")

	def trigger(self):
		try:
			self.startcooldown("ontrigger")
		except AttributeError:
			raise Exception("Tried to trigger() before setcooldown('trigger', seconds)")



class supplymission(mission):

	pass

class deliverymission(mission):
	
	pass