class mission:

	def __init__(self, reward, expectedduration):
		self.reward = reward
		self.expectedduration = expectedduration
		self.cooldownremaining = 0

	def setcooldown(self, seconds, ontrigger):
		if ontrigger:
			self.cooldownontrigger = seconds
		else:
			self.cooldownonfinish = seconds

	def finish(self):
		try:
			if self.cooldownremaining < self.cooldownonfinish:
				self.cooldownremaining = self.cooldownonfinish
		except AttributeError:
			pass

	def trigger(self):
		try:
			if self.cooldownremaining < self.cooldownontrigger:
				self.cooldownremaining = self.cooldownontrigger
		except AttributeError:
			pass


class supplymission(mission):

	pass

class deliverymission(mission):
	
	pass