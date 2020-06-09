class mission:

	def __init__(self, reward, expectedduration, cooldownonfinish):
		self.reward = reward
		self.expectedduration = expectedduration
		self.cooldown = {}
		self.cooldown.onfinish = cooldownonfinish