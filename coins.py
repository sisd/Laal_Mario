from boxes import boxes
from obstacles import obstacles
from land import land

class coins():
	'''@
	'''
	obs = obstacles()
	lnd = land()
	
	block=obs.block
	river=land.river
	coin='@'
	changed_coin='.'

	def __init__(self):
		for i in range(30,1300,30):
			if boxes.box[-5][i] in self.block or boxes.box[-4][i] == self.river:
				continue
			elif boxes.box[-5][i+4] in self.block or boxes.box[-4][i+4] == self.river:
				continue
			elif boxes.box[-5][i+8] in self.block or boxes.box[-4][i+8] == self.river:
				continue
			else:
				for j in [i, i+4, i+8]:
					boxes.box[-6][j] = self.coin