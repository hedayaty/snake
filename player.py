import pygame

from bord import Bord
from snake import Snake

class Player:
	# Initilize
	initial = 4

	def __init__(self, bord, number, name, color, lives):
		self.number = number
		self.color = color
		self.bord = bord
		self.snake = Snake(self.bord.getspawn(self.number), self.initial, self.bord)
		self.lives = lives
#TODO : Later remove this from being hard-coded
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
		self.lives -= 1
		self.snake = Snake(self.bord.getspawn(self.number), self.initial, self.bord)
		return self.lives == 0

	def go(self): return self.snake.go()
	def goup(self):	self.snake.goup()
	def godown(self): self.snake.godown()
	def goright(self): self.snake.goright()
	def goleft(self): self.snake.goleft()

	def usekey (self, key):
		if key in self.keylist.keys():
			self.keylist[key]()

# vim: ts=2 sw=2
