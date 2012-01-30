from bord import Bord
from snake import Snake

class Player:
	# Initilize
	initial = 4

	def __init__(self, bord, number, name, color, lives):
		self.number = number
		self.bord = bord
		self.snake = Snake(self.bord.getspawn(self.number), self.initial, self.bord)
		self.lives = lives

	def die (self):
		self.lives -= 1
		self.snake = Snake(self.bord.getspawn(self.number), self.initial, self.bord)
		return self.lives == 0
# vim: ts=2 sw=2
