from time import time, sleep

class mission:

	def __init__(self, reward, expectedduration):
		self.reward = reward
		self.expectedduration = expectedduration
		self.cooldownend = 0

	def setcooldown(self, event, seconds):
		if event == "trigger":
			self.cooldownontrigger = seconds
		elif event == "finish":
			self.cooldownonfinish = seconds
	
	def startcooldown(self, event):
		if event == "trigger":
			self.cooldownend = time() + self.cooldownontrigger
		elif event == "finish":
			self.cooldownend = time() + self.cooldownonfinish
	
	def getcooldown(self):
		return max(0, self.cooldownend-time())

	def finish(self):
		try:
			self.startcooldown("finish")
		except AttributeError:
			raise Exception("Tried to trigger before setcooldown('finish', seconds)")

	def trigger(self):
		try:
			self.startcooldown("trigger")
		except AttributeError:
			raise Exception("Tried to trigger() before setcooldown('trigger', seconds)")

class supplymission(mission):

	pass

class deliverymission(mission):
	
	pass