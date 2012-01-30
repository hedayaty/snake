import pygame

from bord import Bord
from snake import Snake

class Player:
	# Initilize
	initial = 4

	def __init__(self, bord, number, name, color, lives):
		self.score = 0
		self.number = number
		self.color = color
		self.bord = bord
		self.snake = Snake(self.bord.getspawn(self.number), self.initial, self.bord)
		self.lives = lives
		self.dead = 0

		#TODO : make keys configurable
		if number == 1 :
			self.keylist = {
						pygame.K_DOWN: self.godown,
						pygame.K_UP: self.goup,
						pygame.K_LEFT: self.goleft,
						pygame.K_RIGHT: self.goright,
					}
		elif number == 2 : # So far at most two players
					self.keylist = {
						pygame.K_s: self.godown,
						pygame.K_w: self.goup,
						pygame.K_a: self.goleft,
						pygame.K_d: self.goright,
					}

	def die (self):
		self.score -= 40
		self.lives -= 1
		self.dead = 5
		return self.lives == 0

	def go(self): 
		if self.dead == 1:
			self.snake = Snake(self.bord.getspawn(self.number), self.initial, self.bord)
		if self.dead > 0:		
			self.dead -= 1
		if self.dead == 0 :
			return self.snake.go()
		else: 
			return None

	def goup(self):	self.snake.goup()
	def godown(self): self.snake.godown()
	def goright(self): self.snake.goright()
	def goleft(self): self.snake.goleft()

	def usekey (self, key):
		if key in self.keylist.keys():
			self.keylist[key]()


# vim: ts=2 sw=2
