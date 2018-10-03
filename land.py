from boxes import boxes

class land():
	land_block=['|', 'I']
	river='~'
	spring='s'

	def land_l(self):
		for i in range(0, 1500, 5):
			'''|III|
			   |III|
			'''
			boxes.box[-3][i] = self.land_block[0]
			boxes.box[-3][i+1] = boxes.box[-3][i+2] = boxes.box[-3][i+3] = self.land_block[1]
			boxes.box[-3][i+4] = self.land_block[0]
			boxes.box[-4][i] = self.land_block[0]
			boxes.box[-4][i+1] = boxes.box[-4][i+2] = boxes.box[-4][i+3] = self.land_block[1]
			boxes.box[-4][i+4] = self.land_block[0]
	def river_l(self):
		'''~~~~~~~~~~'''
		for i in range(160, 1300, 250):
			for j in range(10):
				boxes.box[-3][j+i] = self.river
				boxes.box[-4][j+i] = self.river
	def spring_l(self):
		for i in range(50, 60):
			boxes.box[-4][i] = self.spring
	def __init__(self):
		self.land_l()
		self.river_l()
		self.spring_l()