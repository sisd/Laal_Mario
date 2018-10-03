from boxes import boxes

class obstacles():
	'''[lll]
	   [lll]
	   [lll]
	'''
	block=['[', 'l', ']']
	
	mat = [[ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','/','\\',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ' ], 
	[ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','/',' ',' ','\\',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ' ],
	[ ' ',' ',' ',' ',' ',' ','/','\\',' ',' ',' ',' ','/',' ',' ',' ',' ','\\',' ',' ',' ',' ','/','\\',' ',' ',' ',' ',' ',' ' ], 
	[ ' ',' ',' ',' ',' ','/',' ',' ','\\',' ',' ','/',' ',' ',' ',' ',' ',' ','\\',' ',' ','/',' ',' ','\\',' ',' ',' ',' ',' ' ],
	[ ' ','/','\\',' ','D','D','H','H','D','D','D','D','D','D','D','D','D','D','D','D','D','D','H','H','D','D',' ','/','\\',' ' ],
	[ '/',' ',' ','\\','D','D',' ',' ',' ','D','D','D','D','D','D','D','D','D','D','D','D',' ',' ',' ','D','D','/',' ',' ','\\' ],
	[ 'D','H','H','D','D','D',' ',' ',' ','D','D','D','D','D','D','D','D','D','D','D','D',' ',' ',' ','D','D','D','H','H','D' ],
	[ 'D',' ',' ',' ','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D',' ',' ',' ','D' ],
	[ 'D',' ',' ',' ','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D',' ',' ',' ','D' ],
	[ 'D','D','D','D','D','D','D','D','D','D','D','D','D','D',' ',' ','D','D','D','D','D','D','D','D','D','D','D','D','D','D' ],
	[ 'D','D','D','D','D','D','D','D','D','D','D','D','D',' ',' ',' ',' ','D','D','D','D','D','D','D','D','D','D','D','D','D' ],
	[ 'D','D','D','D','H','H','H','D','D','D','D','D',' ',' ',' ',' ',' ',' ','D','D','D','D','D','H','H','H','D','D','D','D' ],
	[ 'D','D','D','D','H','H','H','D','D','D','D','D',' ',' ',' ',' ',' ',' ','D','D','D','D','D','H','H','H','D','D','D','D' ],
	[ 'D','D','D','D','H','H','H','D','D','D','D','D',' ',' ',' ',' ',' ',' ','D','D','D','D','D','H','H','H','D','D','D','D' ],
	[ 'D','D','D','D','D','D','D','D','D','D','D','D',' ',' ',' ',' ',' ',' ','D','D','D','D','D','D','D','D','D','D','D','D' ]]

	def castle(self):
		for i in range(-20, -5, 1):
			for j in range(-60, -30, 1):
				boxes.box[i][j] = obstacles.mat[i+20][j+60]

	def basic_o(self):
		for i in range(60, 1300, 80):
			for k in [i, i+25]:
				for j in [-5,-6,-7]:
					boxes.box[j][k] = self.block[0]
					boxes.box[j][k+1] = boxes.box[j][k+2] = boxes.box[j][k+3] = self.block[1]
					boxes.box[j][k+4] = self.block[2]
		for i in range(160, 1300, 250):
			for j in range(10):
				for k in range(-5,-12,-1):
					boxes.box[k][j+i] = ' '

	def upper_o(self):
		for i in range(100, 1300, 160):
			for j in range(0, 10, 5):
				boxes.box[-10][i+j] = self.block[0]
				boxes.box[-10][i+1+j] = boxes.box[-10][i+2+j] = boxes.box[-10][i+3+j] = self.block[1]
				boxes.box[-10][i+4+j] = self.block[2]

	def next_o(self):
		for k in [390, 815]:
			for j in range(-5,-11,-1):
				boxes.box[j][k] = self.block[0]
				boxes.box[j][k+1] = boxes.box[j][k+2] = boxes.box[j][k+3] = self.block[1]
				boxes.box[j][k+4] = self.block[2]
		for k in [397, 825]:
			for j in range(-5,-14,-1):
				boxes.box[j][k] = self.block[0]
				boxes.box[j][k+1] = boxes.box[j][k+2] = boxes.box[j][k+3] = self.block[1]
				boxes.box[j][k+4] = self.block[2]
		k = 835
		for j in range(-5,-17,-1):
			boxes.box[j][k] = self.block[0]
			boxes.box[j][k+1] = boxes.box[j][k+2] = boxes.box[j][k+3] = self.block[1]
			boxes.box[j][k+4] = self.block[2]
	
	def __init__(self):
		self.basic_o()
		self.next_o()
		self.upper_o()
		self.castle()
