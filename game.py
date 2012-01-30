import sys,pygame,operator
from pygame import *

from bord import Bord
from player import Player

import renderer
#from renderer import updatebord,render

class Game:
	def __init__(self, nplayers, type, lives, mapname):

		# TODO Select Game Type
		# - 1P
		# - 2P
		# - 1P vs AI
		# - 1p vs Network (Master)
		# - Network vs 1p (Slave)
		# TODO Select Bord if needed
		# in case of slave network game this is not needed
		# Get the name of the player + color

		self.bord = Bord("maps/"+ mapname + ".sn")

		# TODO: Pick name/color
		name1 = "Player 1"
		color1 = [ 0, 0, 255] # Blue
		self.players = [Player(self.bord, 1, name1, color1, lives)]

		if nplayers == 2:
			name2 = "Player 2"
			color2 = [ 255, 0, 255] # Red
			self.players.append(Player(self.bord, 2, name2, color2, lives))

		self.type = type
		renderer.updatebord(self.bord)
	

	def mainloop (self):

		clock = pygame.time.Clock()
		# TODO: Trow items on the bord!
		while 1:
			clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					return
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return
					for player in self.players:
						player.usekey (event.key)
						
						
			#TODO: for network game as master, also process keys from client
			#TODO: for network game as slave, also send keys to server

			playerbodies = reduce(operator.add, (player.snake.body for player in self.players))		
	
			for player in self.players:
				head = player.go()
				if head in self.bord.obstacles or head in playerbodies :
					player.die()
				elif head in self.bord.items.keys() :
					pass # TODO

			renderer.render(self.players)
		
# vim: ts=2 sw=2
