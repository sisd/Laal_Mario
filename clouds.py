from boxes import boxes

class clouds():
	'''$$$$$$$
	 ***********
	   $$$$$$$'''
	move_cloud=0
	cloud=[[' ', ' ', '$', '$', '$', '$', '$', '$', '$', ' ', ' '], 
	['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
	['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
	[' ', ' ', '$', '$', '$', '$', '$', '$', '$', ' ', ' ']]
	def birds_1_cl(self):
		initial = [60, 280, 340, 550, 620, 780, 1000, 1240]
		for j in initial:
			for i in range(0, 24, 8):
				boxes.box[14][i+j+1] = '-'
				boxes.box[15][i+j] = '<'; boxes.box[15][i+j+1] = '0'; boxes.box[15][i+j+2] = '<' 
				boxes.box[16][j+i+1] = '^'
	def birds_2_cl(self):
		initial = [60, 280, 340, 550, 620, 780, 1000, 1240]
		for j in initial:
			for i in range(0, 24, 8):
				boxes.box[14][i+j+1] = '-'
				boxes.box[15][i+j] = '>'; boxes.box[15][i+j+1] = '0'; boxes.box[15][i+j+2] = '>' 
				boxes.box[16][j+i+1] = '^'
	def make_cl(self):
		for j in range(4):
			for i in range(11):
				for k in range(30, 1500, 50):
					boxes.box[5+j][(clouds.move_cloud+k+i)%1498+1] = self.cloud[j][i]
				for k in range(10, 1500, 50):
					boxes.box[10+j][(clouds.move_cloud+k+i)%1498+1] = self.cloud[j][i]
	def move_cl(self):
		clouds.move_cloud+=1
		for i in range(30, 1500, 50):
			boxes.box[5][(clouds.move_cloud+i+1)%1498+1] = ' '
			boxes.box[6][(clouds.move_cloud+i-1)%1498+1] = ' '
			boxes.box[7][(clouds.move_cloud+i-1)%1498+1] = ' '
			boxes.box[8][(clouds.move_cloud+i+1)%1498+1] = ' '
		for i in range(10, 1500, 50):
			boxes.box[10][(clouds.move_cloud+i+1)%1498+1] = ' '
			boxes.box[11][(clouds.move_cloud+i-1)%1498+1] = ' '
			boxes.box[12][(clouds.move_cloud+i-1)%1498+1] = ' '
			boxes.box[13][(clouds.move_cloud+i+1)%1498+1] = ' '
	def __init__(self):
		self.make_cl()
		self.move_cl()
		if (clouds.move_cloud%2 == 0):
			self.birds_1_cl()
		else:
			self.birds_2_cl()

