from boxes import boxes
from obstacles import obstacles
from point import person

class enemies(person):
	'''##
	'''
	obs=obstacles()

	block=obs.block
	enemy_pos=0
	flag=0
	enemy=['#', '#']
	enemy_0='#'
	enemy_1='`'
	ret_value=0
	enemy_store = [['#', '#'], ['#', '#'], ['#', '#'], ['#', '#'], 
	['#', '#'], ['#', '#'], ['#', '#'], ['#', '#'], 
	['#', '#'], ['#', '#'], ['#', '#'], ['#', '#'], 
	['#', '#'], ['#', '#'], ['#', '#'], ['#', '#'], 
	['#', '#'], ['#', '#'], ['#', '#'], ['#', '#'], 
	['#', '#'], ['#', '#'], ['#', '#'], ['#', '#']]

	def flag_check_e(self):
		if boxes.box[-5][83-enemies.enemy_pos-2] in enemies.block:
			enemies.flag=1
		elif boxes.box[-5][83-enemies.enemy_pos+3] in enemies.block:
			enemies.flag=0
	
		#front move
	def moveleft_e(self):
		enemies.enemy_pos+=1
		for i in range(85, 1300, 80):
			boxes.box[-5][i-enemies.enemy_pos] = ' '
			if (boxes.box[-5][i-3-enemies.enemy_pos] == ' ' or enemies.enemy_store[(i-85)//80][0] == enemies.enemy_1):
				boxes.box[-5][i-enemies.enemy_pos-1] = enemies.enemy_store[(i-85)//80][1]
				boxes.box[-5][i-enemies.enemy_pos-2] = enemies.enemy_store[(i-85)//80][0]
			else:
				enemies.enemy_store[(i-85)//80][1] = enemies.enemy_store[(i-85)//80][0] = enemies.enemy_1
				boxes.box[-5][i-enemies.enemy_pos-1] = enemies.enemy_1
				boxes.box[-5][i-enemies.enemy_pos-2] = enemies.enemy_1
				enemies.enemy_pos-=1 
				enemies.ret_value = 2
	def moveright_e(self):
		enemies.enemy_pos-=1
		for i in range(85, 1300, 80):
			boxes.box[-5][i-enemies.enemy_pos-3] = ' '
			if (boxes.box[-5][i-enemies.enemy_pos] == ' ' or enemies.enemy_store[(i-85)//80][0] == enemies.enemy_1):
				boxes.box[-5][i-enemies.enemy_pos-2] = enemies.enemy_store[(i-85)//80][0]
				boxes.box[-5][i-enemies.enemy_pos-1] = enemies.enemy_store[(i-85)//80][1]
			else:
				enemies.enemy_store[(i-85)//80][1] = enemies.enemy_store[(i-85)//80][0] = enemies.enemy_1
				boxes.box[-5][i-enemies.enemy_pos-2] = enemies.enemy_1
				boxes.box[-5][i-enemies.enemy_pos-1] = enemies.enemy_1
				enemies.enemy_pos+=1
				enemies.ret_value = 2	
	
	def __init__(self):
		person.__init__(self, enemies.enemy_pos, -5)
		enemies.ret_value = 0
		self.flag_check_e()
		if enemies.flag == 0:
			self.moveleft_e()
		else:
			self.moveright_e()

#enemies_2(0)