import colorama
from os import system
from input import Input
from time import sleep
from boxes import boxes
from clouds import clouds
from mountains import mountains
from land import land
from obstacles import obstacles
from enemies import enemies
from marios import marios
from coins import coins
#from Boss import boss

#bos = boss()
mtn = mountains()
con = coins()
obs = obstacles()
lnd = land()
ino = Input()
bxx = boxes()
cld = clouds()
mro = marios('0')
ene = enemies()

death=0
x=0
gravity=0
ite=0
time_points=10000

def die():
	system('clear')
	for i in range(10):
		print('')
	for i in range(50):
		print(' ', end='')
	print("BBBBB          OOOO           OOOO       MMM      MMM")
	for i in range(50):
		print(' ', end='')
	print("BB  BBB      OO    OO       OO    OO     MMMMM  MMMMM")
	for i in range(50):
		print(' ', end='')
	print("BB  BBBB    OOO    OOO     OOO    OOO    MMM  MM  MMM")
	for i in range(50):
		print(' ', end='')
	print("BBBBBB     OOOO    OOOO   OOOO    OOOO   MMM      MMM")
	for i in range(50):
		print(' ', end='')
	print("BB  BBBB    OOO    OOO     OOO    OOO    MMM      MMM")
	for i in range(50):
		print(' ', end='')
	print("BB  BBB      OO    OO       OO    OO     MMM      MMM")
	for i in range(50):
		print(' ', end='')
	print("BBBBB          OOOO           OOOO       MMM      MMM")

def color_choice(i, j):
	if boxes.box[i][j] in ['o', '-', '+', '\'']:
		print('\033[37m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] == 'H':
		print('\033[96m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] in ['[', 'l', ']']:
		print('\033[92m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] in ['@', '.']:
		print('\033[33m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] in ['#']:
		print('\033[35m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] in ['|', 'I']:
		print('\033[94m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] in ['$', '*']:
		print('\033[36m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] in ['<', '>', '^', '0', 'v']:
		print('\033[31m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] in ['/', '\\']:
		print('\033[91m' + boxes.box[i][j], end='')
	elif boxes.box[i][j] == '`':
		print('\033[30m' + boxes.box[i][j], end='')
	else:
		print(boxes.box[i][j], end='')
	print('\033[0m', end='')

die_flag=0

while(1):
	system("clear")

	#print(marios.mario_pos_y)
	if boxes.box[marios.mario_pos_y+3][marios.mario_pos_x] == land.spring or boxes.box[marios.mario_pos_y+3][marios.mario_pos_x+2] == land.spring:
		marios('w')
		for i in range(5): 
			marios('w'); marios('d')
		gravity+=1
	if marios.mario_pos_y < -7:
		gravity+=1
		if gravity == 3:
			marios('l')
			gravity=0
	if boxes.box[marios.mario_pos_y+3][marios.mario_pos_x] == land.river or boxes.box[marios.mario_pos_y+3][marios.mario_pos_x+2] == land.river:
		#marios('l')
		death+=1
		#print("gaand me danda")
		die()
		for i in range(4):
			marios('d')
		marios('w')
		sleep(1)
	if marios.mario_pos_x >= boxes.frame and boxes.frame != 1450:
		x+=50
		boxes.frame+=50
	if ino.input():
		cin=ino.getch()
		if cin == 'q':
			break;
		#print(cin)
		marios(cin)
	else:
		#if (boxes.frame == 1400) and die_flag==0:
		#	boss()
		#if die_flag==1:
		#	die_flag=0
		#for j in range(3):
		#	for i in range(150):
		#		print(mario_logo[j][i])
		#for x in range(0,1500,150):
		for i in range(40):
			for j in range(x, x+150):
				color_choice(i, j)
			print('')
		print("\n\n")
		clouds()
		ite+=1
		check=0
		print(boxes.frame)
		if ite%2==0:
			enemies()
			if enemies.ret_value == 2:
				death+=1
				#print("teri gaand me danda")
				die()
				sleep(1)
		if marios.death_flag == 1:
			marios.death_flag=0
			death+=1
			#print("teri gaand me danda")
			#if boss.boss_kill == 1:
			#	die_flag=1
			#	boss.boss_kill=0
			#	marios('w')
			die()
			sleep(1)
		print("Points = ", marios.mario_pos_x*10+marios.kill*300+marios.hand_coin*100+time_points-ite*10, " coins in hand = ", marios.hand_coin, " kills = ", marios.kill, " deaths = ", death)
		if death == 10:
			break;
		sleep(0.1)
		#break

print("Game Over")