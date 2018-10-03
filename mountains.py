from boxes import boxes

class mountains():
	''' 	  /\
			//  \\
		  ///	 \\\
		////	  \\\\
	  /////		   \\\\\
	//////			\\\\\\
  ///////			 \\\\\\\
////////			  \\\\\\\\
	'''
	mountain=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '/', ' ', ' ', '\\', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '/', '/', ' ', ' ', ' ', ' ', '\\', '\\', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '/', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', '\\', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ', ' ', '/', '/', '/', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', '\\', '\\', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', '/', '/', '/', '/', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', '\\', '\\', '\\', '\\', ' ', ' ', ' ', ' ', ' '],
	[' ', ' ',  '/', '/',  '/',  '/',  '/',  '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', '\\', '\\', '\\', '\\', '\\', ' ', ' ', ' '],
	['/', '/', '/', '/', '/', '/', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', '\\', '\\', '\\', '\\', '\\', '\\']]
	def up_mt(self):
		for i in range(8):
			for j in range(30):
				for k in range(25, 1280, 35):
					boxes.box[-18+i][k+j] = self.mountain[i][j]
	def down_mt(self):
		for i in range(8):
			for j in range(30):
				for k in range(5, 1300, 35):
					boxes.box[-13+i][k+j] = self.mountain[i][j]
	def __init__(self):
		self.up_mt()
		self.down_mt()