import sys,pygame,operator,random, itertools, os
from pygame import *

from player import Player

import renderer, bord, menu

otheritemtypes = ["R", " ", "P"]

#################### Initilize Game #########################
# Input: number of player, typeof game, player lives, map file name
# Initilizes a game with the given parameters
# Supposed to choose names and color for players
def init(gametype, lives):
	global players, items
	# Use Game Type
	# - 1P
	# - 2P
	# - 1P vs AI
	# - 1p vs Network (Master)
	# - Network vs 1p (Slave)
	if gametype == "1p" : 
		nplayers = 1
	else :
		nplayers = 2
		
	if gametype != "slave" :
		list = os.listdir("maps")
		list.sort()
		mapname = menu.choose (zip(list,list))
		if mapname == None :
			return False

	# TODO Get the name of the player + color

	bord.init ("maps/"+ mapname)
	items = {}

	# TODO: Pick name/color
	name1 = "Player 1"
	players = [Player("keypad", bord.spawn[1], name1, renderer.blue, lives)]

	if nplayers == 2:
		name2 = "Player 2"
		if gametype == "ai":
			dev2 = "ai"
		elif gametype == "master":
			dev2 = "net"
		else:
			dev2 = "keybord"
			
		players.append(Player(dev2, bord.spawn[2], name2, renderer.pink, lives))

	renderer.updatebord()
	return True

###################### Place #########################################
# Input: type of item
# Output: place of item
# Places an item of type in a free spot with default timeout 300
def place (type):
	blocked = playerbodies + \
						bord.obstacles +\
						items.keys()
	dim = bord.dim
	loc = blocked[0]
	while loc in blocked:
		loc = random.randint (0, dim[0] - 1),\
						random.randint (0, dim[1] - 1)

	items[loc] = {"type" : type, "timer" : 300}
	return loc

######################## Spawn ###################################
# Input: void
# Ouput: a free location for player spawn
def spawn():
	blocked = set(playerbodies + \
						bord.obstacles +\
						items.keys())
	dim = bord.dim
	margin = 5
	tries = 0
	while 1:
		loc = random.randint (margin, dim[0] - margin - 1),\
					random.randint (margin, dim[1] - margin - 1)
		if set(tuple(map(operator.add, neib, loc))\
				for	neib in itertools.product (range(-margin, margin+1), repeat=2)
				) &	blocked :
			tries += 1
			if tries == dim[0] * dim[1]: # Almost all the bord!
				tries = 0
				margin -= 1
				# hopefully, margins will never too small
		else :
			break
	return loc
		
def mainloop ():
	global playerbodies, items, gameover, clock, digplace
	digit = 1
	clock = pygame.time.Clock()

	playerbodies = reduce(operator.add, (player.snake.body[:] for player in players))	

	# TODO: Trow more items on the bord!
	digplace = place(str(digit))
	gameover = False

	while 1:
		clock.tick(10)

		# Render the screen
		renderer.render()

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return
				for player in players:
					player.usekey (event.key)

		if gameover:
			continue

		for player in players:	
			if player.dev == "ai":
				player.aimove()
					
		#TODO: for network game as master, also process keys from client
		#TODO: for network game as slave, also send keys to server


		for player in players:
			head = player.go()

			# Check if hit the wall or ther players
			if head in bord.obstacles or head in playerbodies : 
	#			print "head", head
	#			print "obstacles", bord.obstacles
		#		print "bodies", playerbodies
				if digit > 5:
					digit -= 4
				else:
					digit = 1
				items[digplace]["type"] = str(digit)
				if player.die() :
					gameover = True
					break

			# Check if hit any items
			elif head in items.keys() :
				# TODO: Assumed items are only numbers
				del items[head]
				player.score += 10 * digit
				player.snake.grow(digit * 4)
				digit += 1
				if digit == 10:
					gameover = True
					break
				else:
					digplace = place (str(digit))
			

		# keep track of player bodies as obstacles as well
		playerbodies = reduce(operator.add, (player.snake.body[:] for player in players))		

		# Check for timer exppirations
		for loc in items.keys() :
			item = items[loc]
			item["timer"] -= 1
			if item["timer"] == 0 :
				type = item["type"]
				del item
				if type in otheritemtypes :
					place (random.choice(otheritemtypes))
				else: # It is number, put the same number somewhere else on the bord
					digplace = place (type)

			
	
# vim: ts=2 sw=2
