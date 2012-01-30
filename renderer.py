import pygame
from pygame import *
from bord import Bord
from player import Player
from snake import Snake
#from game import Game

class Renderer:
	def __init__ (self, size) :
		self.size = size
		self.screen = pygame.display.set_mode(size)
		self.black = 0,0,0
	
	def updatebord (self, bord) :
		self.bord = bord
		self.bordimage = pygame.Surface(self.size)
		for pixel in self.bord.obstacles :
			pass

	def render(self):
		self.screen.fill(self.black)
		self.screen.blit(self.bordimage, [0]*2)
		pygame.display.flip()

# vim: ts=2 sw=2
