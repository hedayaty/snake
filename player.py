import pygame,operator,itertools

import game,board

class Player:
	# Initilize
	initial = 4
	deadtimer = 5
################################ Init #####################
# Input:  player name, controller device, player color, player initial lives
# Initialized player
	def __init__(self, name, dev, color, lives):
		self.name = name
		self.dev = dev
		self.color = color
		self.lives = lives
		self.score = 0
		self.playing = True

		self.path = []

		if self.dev == "keypad" :
			self.keylist = {
						pygame.K_DOWN: self.godown,
						pygame.K_UP: self.goup,
						pygame.K_LEFT: self.goleft,
						pygame.K_RIGHT: self.goright,
					}
		elif self.dev == "keyboard" :
			self.keylist = {
						pygame.K_s: self.godown,
						pygame.K_w: self.goup,
						pygame.K_a: self.goleft,
						pygame.K_d: self.goright,
					}
		elif self.dev == "vim" :
			self.keylist = {
					pygame.K_h: self.goleft,
					pygame.K_j: self.godown,
					pygame.K_k: self.goup,
					pygame.K_l: self.goright,
				}
		else: 
			self.keylist = {}
			

############################ Die ################################
# Input: void
# Output: if player has any more lives
	def die (self):
		for point in self.body[0:-1]:
			game.blocked.remove(point)
		self.score -= 40
		self.lives -= 1
		self.dead = self.deadtimer
		self.path = []
		return self.lives == 0

############################ GO ###################################
# Input: void
# Output: head if player is alive; otherwise, none
# Go ahead using dir, if there is potential to grow then  grow
	def go(self): 
		# Reduce timer if dead
		if self.dead > 0:		
			self.dead -= 1
			# If dead timer ended, respawn
			if self.dead == 0:
				self.start ()
			return None

		head = self.gethead()
		head = board.progress(head, self.dir)
		self.body.append (head)
		if self.growable > 0 :
			self.growable -= 1
		else :
			game.blocked.remove(self.body.pop(0))
		self.useddir = self.dir	
		return head

##################### Start ######################################
# Input: void
# Spawn player and craete snake
	def start (self):
		if self.lives == 0:
			self.go = lambda : None
			self.aimove = lambda : None
			self.body = []
			self.playing = False
			game.remplayers -= 1
			return
		self.body = [game.spawn()]
		self.growable = self.initial
		self.dir = board.defaultdir
		self.useddir = self.dir
		self.dead = 0

############################# Get Head	###################################
# Input: void
# Get the head
	def gethead (self):
		return self.body[-1]


######################### Reverse ########################################
# Input: void
# Reverse the snake, happens when opponent easts special item
	def reverse (self):
		body.reverse()

######################### Go Up,Down,Right, Left  ########################
# Input: void
# Change direction to up/down/right/left
	def goup (self):
		if self.useddir != board.down :
			self.dir = board.up

	def godown (self):
		if self.useddir != board.up :
			self.dir = board.down

	def goright (self):
		if self.useddir != board.left :
			self.dir = board.right

	def goleft (self):
		if self.useddir != board.right :
			self.dir = board.left

########################### Grow ###############################################
# Input: length
# Add the amount the potential growth
	def grow (self, length) :
		self.growable += length
		
####################### Use key ###################################
# Input: key
# Change direction is key is for me
	def usekey (self, key):
		if key in self.keylist.keys():
			self.keylist[key]()

###################### Get Neighbors #################################
# Input: point
# Output: Non-blocked neighbors
	def getneighbors (self, point):
		return set([ (board.progress (point, dir)) for dir in board.dirs]) - game.blocked

######################  AI Move ##############################
# Input: void
# Selects a move for AI, if the old path is useable follow that; otherwise,
# find a new path
	def aimove(self):
		if self.dead > 0:
			return
		start = self.gethead()
		end = game.digplace
	
		# If old path is ok, continue!
		last = None
		if self.path == [] or self.path[-1] != end or set(self.path) & game.blocked != set():	
			# Use BFS
			moves = self.getneighbors(start) 
			parrent = {start:None}
			for move in list(moves):
				parrent[move] = start
			mark = set([start]) | moves
			while moves :
				next = set()
				for move in list(moves) :
					for point in self.getneighbors(move) :
						if point not in mark:
							next.add(point)
							mark.add(point)
							parrent[point] = move
							last = point
				moves = next

			# Find the path
			if end in mark:
				node = end
			elif last == None:
				return #Soon to be dead!
			elif board.progress(start, self.dir) in game.blocked: # Try to survie as long as possible
				node = last 
			else:
				node = None
			if node != None:
				self.path = []
				while parrent[node]:
					self.path.append(node)
					node = parrent[node]
				self.path.reverse()
		if len(self.path) > 0:
			self.dir = tuple(map(operator.sub, self.path.pop(0), start))
#			self.path.pop(0)
#		{ board.up: self.goup, board.down:self.godown, board.left: self.goleft, board.right: self.goright }[dir]()
		
# vim: ts=2 sw=2
