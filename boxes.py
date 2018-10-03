class boxes():
	'''MAIN BOARD CLASS'''
	frame = 100
	box = [[' ']*1500]
	for i in range(40):
		box.append([' ']*1500)

	#boundary walls
	for i in range(1500):
		box[0][i] = '^'
		box[39][i] = 'v'
	for i in range(40):
		box[i][0] = '|'
		box[i][1499] = '|'