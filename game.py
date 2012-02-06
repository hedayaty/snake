import sys,pygame,operator,random, itertools, os
from pygame import *

import renderer, board, menu, network
from player import Player

# TODO: other items not used!
otheritemtypes = ["R", " ", "P"]

#################### Initilize Game #########################
# Input: number of player, typeof game, player lives, map file name
# Initilizes a game with the given parameters
# Supposed to choose names and color for players
def init(gametype):
	global players, items
	global ucolors, udevs, devs, colors
	global numbersend, lives, netgame
	global blue, pink, green, red, orange,cyan
	global nlpr, cont

	blue = (0,0,255)
	pink = (255,20,147)
	green =(0,128,0)
	red = (255,0,0)
	orange = (255,165,0)
	cyan= (0,255,255)
	

	if gametype != "join" :
		list = os.listdir("maps")
		list.sort()
		mapname = menu.choose ("Select the map:",\
					[{ "label" : file, "value" : file} for file in list])
		if mapname == None :
			return False

		board.init ("maps/"+ mapname)
		items = {}
	
	# Get Game options
	boolean = [ { "label" : "On", "value": True }, 
							{ "label" : "Off", "value": False } 
						]
	multioptions = [																								\
			{ "description" : "NLPR: ", 																\
				"name" : "nlpr", 																					\
				"options" : boolean,																			\
				"default" : False,																				\
			}, 																													\
			{	"description" : "Continue: ",															\
				"name" : "cont", 																					\
				"options" : boolean,																			\
				"default" : False,																				\
			},																													\
			{ "description" : "End with numbers: ",											\
				"name" : "numbersend",																		\
				"options" : boolean,																			\
				"default" : True,																					\
			},																													\
			{	"description" : "Players: ",															\
				"name" : "nplayers",																			\
				"default" : 2,																						\
				"options" : [ { "label" : str(x), "value" : x} 						\
												for x in range(1,7)												\
										]																							\
			}]

	if gametype == "1p":
		multioptions = []

	options = menu.select ("Select Game Options",										\
			multioptions + 																							\
			[{	"description" : "Lives: ", 															\
					"name" : "lives", 																			\
					"default" : 5,																					\
					"options" : [ { "label" : str(x), "value" : x }					\
						for x in [1, 2, 3, 4, 5, 10, 20, 50, 64, 100, 256]]} 	\
			])
	if options == None:
		return False
	if gametype == "1p":
		nlpr = False
		cont = False
		nplayers = 1
		numbersend = True
	else:
		nlpr = options["nlpr"]["value"]
		cont = options["cont"]["value"]
		nplayers = options["nplayers"]["value"]
		numbersend = options["numbersend"]["value"]
	lives = options["lives"]["value"]

	# Get Players
	ucolors = set()
	udevs = set()
	colors = [blue, pink, green, red, orange, cyan]
	devs = [("Keypad", "keypad"), ("Keyboard (wasd)", "keyboard"),		\
					("Vim Keys (hjjkl)", "vim"), 															\
					("Computer", "ai"), ("Netwrok", "net")]

	players = []
	netgame = False
	for i in range(nplayers):
		player = getplayer(str(i+1))
		if player == None:
			return None
		players.append(player)

	if netgame:
#		network.startserver()
		for player in players:
			if player.dev == "net":
				if network.waitfor(player) == None:
					network.sendinfo (player, board.dim, board.obstacles)
					return None
			
	renderer.updateboard()
	return True

######################### Get Player #################################
# Input: void
# Output: Player instance
def getplayer(pnum):
	global netgame
	menuname = { "name" : "name", "label" : "Player " + pnum , "description" : "Name: "}
	menudev = { "description" : "Control: ", 									\
							"name" : "dev", 																\
							"options": 																			\
							[ { "label" : label, "value": dev } 						\
								for label,dev in devs if dev not in udevs			\
							] 																							\
						}
	menucolor = { "name" : "color", 
								"options" : 
								[ {"label" : "color", "value" : color } 
									for color in colors if color not in ucolors
								] 
							}

	values =  menu.select ("Select Player " + pnum,	[ menuname, menudev, menucolor ])
	if values == None:
		return None

	color = values["color"]["value"]
	name = values["name"]
	dev = values["dev"]["value"]

	ucolors.add(color)
	# Same players can not use the same device but ai and net are ok!
	if dev not in [ "ai", "net" ]:
		udevs.add(dev)
	if dev == "net":
		netgame = True
	return Player (name, dev, color, lives)

###################### Place #########################################
# Input: type of item
# Output: place of item
# Places an item of type in a free spot with default timeout 300
def place (type):
	dim = board.dim
	while 1:
		loc = random.randint (0, dim[0] - 1),\
						random.randint (0, dim[1] - 1)
		if loc not in blocked:
			break

	items[loc] = {"type" : type, "timer" : 300}
	return loc

######################## Spawn ###################################
# Input: void
# Ouput: a free location for player spawn
def spawn():
	dim = board.dim
	margin = 5
	tries = 0
	while 1:
		loc = random.randint (margin, dim[0] - margin - 1),\
					random.randint (margin, dim[1] - margin - 1)
		ranges = itertools.product (range(-margin, margin+1), repeat=2)

		if set(tuple(map(operator.add, neib, loc))\
				for	neib in ranges	) &	blocked :
			tries += 1
			if tries == dim[0] * dim[1]: # Almost all the board!
				tries = 0
				margin -= 1
				# hopefully, margins will never too small
		else :
			break
	return loc
		
def mainloop ():
	global items, gameover, clock, digplace
	global blocked, playerheads
	digit = 1
	clock = pygame.time.Clock()
	
	blocked = set(board.obstacles)
#	playerbodies = []
	for player in players:
		player.start ()

	# TODO: Trow more items on the board!
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
			elif player.dev == "net":
				network.getkey (player)
				network.sendinfo (player, players, items)

		for player in players:		
			if player.dead == 0:
				blocked.add(player.gethead())
		playerheads = []
		dead = set()
		for player in players:
			head = player.go()
			# Check if hit the wall or ther players
			if head in blocked:
				if digit > 5:
					digit -= 4
				else:
					digit = 1
				items[digplace]["type"] = str(digit)
				if nlpr:
					for other in players:
						if other != player:
							if head in other.body:
								other.grow (len(player.body))
				dead.add(player)

			# Check if hit any items
			elif items.has_key(head) :
				# TODO: Assumed items are only numbers
				del items[head]
				player.score += 10 * digit
				player.grow(digit * 4)
				digit += 1
				if digit < 10 or not numbersend:
					if digit == 10:
						digit = random.randint(1,6)
					digplace = place (str(digit))
				else:
					gameover = True
			playerheads.append(head) # Use this to detect head-to-head
		# Detect head-to-head
		for player1 in players:
			if player1.dead == 0 and playerheads.count(player.gethead()) > 1:
				dead.add(player1)

		# Now see who is dead	
		for player in list(dead):
			if player.die():
				if cont:
					players.remove(player)
				else:
					gameover = True
		# Do not go on without players!
		if players == []:
			gameover = True
			continue
						
		# keep track of player bodies as obstacles as well
		#playerbodies = reduce(operator.add, (player.body[:] for player in players))		

		# Check for timer exppirations
		for loc in items.keys() :
			item = items[loc]
			item["timer"] -= 1
			if item["timer"] == 0 :
				type = item["type"]
				del items[loc]
				if type in otheritemtypes :
					place (random.choice(otheritemtypes))
				else: # It is number, put the same number somewhere else on the board
					digplace = place (type)

			
	
# vim: ts=2 sw=2
