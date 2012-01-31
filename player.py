import pygame

from snake import Snake

import game

class Player:
	# Initilize
	initial = 4
	deadtimer = 5
################################ Init #####################
# Input: Spawn location, player name, player color, player initial lives
# Initilized player
	def __init__(self, dev, spawn, name, color, lives):
		self.name = name
		self.score = 0
		self.color = color
		self.snake = Snake(spawn, self.initial)
		self.lives = lives
		self.dead = 0

		#TODO : make keys configurable
		if dev == "keypad" :
			self.keylist = {
						pygame.K_DOWN: self.godown,
						pygame.K_UP: self.goup,
						pygame.K_LEFT: self.goleft,
						pygame.K_RIGHT: self.goright,
					}
		elif dev == "keybord" : # So far at most two players
			self.keylist = {
						pygame.K_s: self.godown,
						pygame.K_w: self.goup,
						pygame.K_a: self.goleft,
						pygame.K_d: self.goright,
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
		return self.lives == 0

############################ GO ###################################
# Input: go ahead
# Output: head if player is alive; otherwise, none
	def go(self): 
		if self.dead == 1:
			self.snake = Snake(game.spawn(), self.initial)
		if self.dead > 0:		
			self.dead -= 1
		if self.dead == 0 :
			return self.snake.go()
		else: 
			return None

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

###################### Make AI Move ##############################
	def aimove(self):
		start = self.snake.gethead()
		end = game.digplace
		
		def getneighbors ((point,cost)):
			return [ (bord.progess (point, dir), cost + 1) for dir in [bord.up, bord.down, bord.left, bord.right]\
				 if not bord.progess (point, dir) in bord.obstacles + game.playerbodies ]

		moves = getneighbors((start,0))
		
		
		
# vim: ts=2 sw=2
