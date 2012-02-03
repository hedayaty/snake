import pygame,operator,itertools
from snake import Snake

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
		self.score -= 40
		self.lives -= 1
		self.dead = self.deadtimer
		self.path = []
		return self.lives == 0

############################ GO ###################################
# Input: go ahead
# Output: head if player is alive; otherwise, none
	def go(self): 
		if self.dead == 1:
			self.start ()
		if self.dead > 0:		
			self.dead -= 1
		if self.dead == 0 :
			return self.snake.go()
		else:
			return None

##################### Start ######################################
# Input: void
# Spawn player and craete snake
	def start (self):
		self.snake = Snake(game.spawn(), self.initial)
		self.dead = 0
		

###################### GoUp, GoDown, GoLeft, GoRight ##############
	def goup(self):	self.snake.goup()
	def godown(self): self.snake.godown()
	def goright(self): self.snake.goright()
	def goleft(self): self.snake.goleft()

####################### Use key ###################################
# Input: key
# Change direction is key is for me
	def usekey (self, key):
		if key in self.keylist.keys():
			self.keylist[key]()

######################  AI Move ##############################
# Input: void
# Selects a move for AI, if the old path is useable follow that; otherwise,
# find a new path
	def aimove(self):
		if self.dead > 0:
			return
		start = self.snake.gethead()
		end = game.digplace
		blocked = set (board.obstacles + game.playerbodies)
		def getneighbors (point):
			return [ (board.progress (point, dir)) for dir in [board.up, board.down, board.left, board.right]\
				 if board.progress (point, dir) not in blocked ]
	
		# If old path is ok, continue!
		if self.path == [] or self.path[-1] != end or set(self.path) & set(game.playerbodies) != [] :	
			# Use BFS
			moves = getneighbors(start) 
			parrent = {start:None}
			for move in moves:
				parrent[move] = start
			mark = set([start]) | set(moves)
			while moves :
				next = []
				for move in moves :
					for point in getneighbors(move) :
						if point not in mark:
							next.append(point)
							mark.add(point)
							parrent[point] = move
				moves = next
				if end in mark:
					break
			# If there is no path do nothing!
			if end not in mark:
				self.path = []
				return

			# Find the path
			node = end
			self.path = []
			while parrent[node]:
				self.path.append(node)
				node = parrent[node]
			
			self.path.reverse()

		dir = tuple(map(operator.sub, self.path[0], start))
		self.path.pop(0)
		{ board.up: self.goup, board.down:self.godown, board.left: self.goleft, board.right: self.goright }[dir]()
		
# vim: ts=2 sw=2
