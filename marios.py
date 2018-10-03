from boxes import boxes
from coins import coins
from obstacles import obstacles
from enemies import enemies
from point import person

class marios(person):
	'''o
	  -H-
	  +'+
	'''
	coi=coins()
	b=boxes()
	obs=obstacles()
	ene=enemies()
	
	coin=coi.coin
	changed_coin=coi.changed_coin
	block=obs.block
	enemy_0=ene.enemy_0
	enemy_1=ene.enemy_1

	boss_defeat=0
	mario_pos_x=40
	mario_pos_y=-7
	hand_coin=0
	mario=[[' ', 'o', ' '], ['-', 'H', '-'], ['+', '\'', '+']]
	store=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	dif_x=dif_y=0
	death_flag=0
	kill=0
	
	def coins_m(self, inp):
		if (boxes.box[marios.mario_pos_y+1][marios.mario_pos_x+3] == marios.coin and inp == 'd'):
			boxes.box[marios.mario_pos_y+1][marios.mario_pos_x+3] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+1][marios.mario_pos_x-1] == marios.coin and inp == 'a'):
			boxes.box[marios.mario_pos_y+1][marios.mario_pos_x-1] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+1][marios.mario_pos_x+4] == marios.coin and inp == 'd'): 
			boxes.box[marios.mario_pos_y+1][marios.mario_pos_x+4] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+1][marios.mario_pos_x-2] == marios.coin and inp == 'a'):
			boxes.box[marios.mario_pos_y+1][marios.mario_pos_x-2] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+1][marios.mario_pos_x+5] == marios.coin and inp == 'd'):
			boxes.box[marios.mario_pos_y+1][marios.mario_pos_x+5] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+1][marios.mario_pos_x-3] == marios.coin and inp == 'a'):
			boxes.box[marios.mario_pos_y+1][marios.mario_pos_x-3] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+4][marios.mario_pos_x-1] == marios.coin and inp == 'l'):
			boxes.box[marios.mario_pos_y+4][marios.mario_pos_x-1] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+4][marios.mario_pos_x-2] == marios.coin and inp == 'l'):
			boxes.box[marios.mario_pos_y+4][marios.mario_pos_x-2] = marios.changed_coin
			marios.hand_coin+=1
		elif (boxes.box[marios.mario_pos_y+4][marios.mario_pos_x-3] == marios.coin and inp == 'l'):
			boxes.box[marios.mario_pos_y+4][marios.mario_pos_x-3] = marios.changed_coin
			marios.hand_coin+=1

	def frame_check_m(self, inp):
		if marios.mario_pos_x<(boxes.frame-97):
			if inp == 'a':
				return 3
		if marios.mario_pos_x >= 1445 and marios.boss_defeat != 1:
			if inp == 'd':
				return 3

	def obstacles_m(self, inp):
		#not passing through tubes
		if boxes.box[marios.mario_pos_y+2][marios.mario_pos_x+5] in [*marios.block, marios.enemy_0]:
			if inp == 'd':
				return 3
		if boxes.box[marios.mario_pos_y+2][marios.mario_pos_x-3] in [*marios.block, marios.enemy_0]:
			if inp == 'a':
				return 3
	
		#standing on tubes
		if boxes.box[marios.mario_pos_y+3][marios.mario_pos_x] in marios.block or boxes.box[marios.mario_pos_y+3][marios.mario_pos_x+2] in marios.block:
			if inp == 'l':
				return 3
	
	def start_m(self):
		for i in range(3):
			for j in range(3):
				marios.store[i][j] = boxes.box[-7+i][marios.mario_pos_x+j]
				boxes.box[-7+i][marios.mario_pos_x+j] = marios.mario[i][j]
	
	def input_m(self, inp):
		if inp == 'w':
			marios.mario_pos_y-=3
			marios.dif_y=3	
		elif inp == 'l':
			if boxes.box[marios.mario_pos_y+5][marios.mario_pos_x] == marios.enemy_0 or boxes.box[marios.mario_pos_y+5][marios.mario_pos_x+2] == marios.enemy_0:
				enemies.enemy_store[(marios.mario_pos_x-5)//80][1] = enemies.enemy_store[(marios.mario_pos_x-5)//80][0] = marios.enemy_1
				marios.kill+=1
			marios.mario_pos_y+=3
			marios.dif_y=-3	
		elif inp == 'a':
			if boxes.box[marios.mario_pos_y+2][marios.mario_pos_x-2] == marios.enemy_0 or boxes.box[marios.mario_pos_y+2][marios.mario_pos_x-3] == marios.enemy_0:
				enemies.enemy_store[(marios.mario_pos_x-5)//80][1] = enemies.enemy_store[(marios.mario_pos_x-5)//80][0] = marios.enemy_1
				marios.death_flag=1
			marios.mario_pos_x-=3
			marios.dif_x=-3	
		elif inp == 'd':
			if boxes.box[marios.mario_pos_y+2][marios.mario_pos_x+4] == marios.enemy_0 or boxes.box[marios.mario_pos_y+2][marios.mario_pos_x+5] == marios.enemy_0:
				enemies.enemy_store[(marios.mario_pos_x-5)//80][1] = enemies.enemy_store[(marios.mario_pos_x-5)//80][0] = marios.enemy_1
				marios.death_flag=1
			marios.mario_pos_x+=3
			marios.dif_x=3
	
	def move_m(self):
		for i in range(3):
			for j in range(3):
				boxes.box[marios.mario_pos_y+marios.dif_y+i][marios.mario_pos_x+j-marios.dif_x] = marios.store[i][j]
				marios.store[i][j] = boxes.box[marios.mario_pos_y+i][marios.mario_pos_x+j]
				boxes.box[marios.mario_pos_y+i][marios.mario_pos_x+j] = marios.mario[i][j]
	
	def __init__(self, inp):
		marios.dif_x=marios.dif_y=marios.death_flag=0
		person.__init__(self, marios.mario_pos_x, marios.mario_pos_y)
		if inp == '0':
			self.start_m()
		self.coins_m(inp)
		if self.frame_check_m(inp) == 3:
			return
		if self.obstacles_m(inp) == 3:
			return
		if self.input_m(inp) == 3:
			return
		self.move_m()