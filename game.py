import sys,pygame,operator
from pygame import *

from bord import Bord
from player import Player
from renderer import Renderer

class Game:
	def __init__(self, renderer, nplayers, type, lives, mapname):

		self.renderer = renderer
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

		ended = False
		clock = pygame.time.Clock()
		# TODO: Trow items on the bord!

		while ended == False:
			clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						print "Hit Espace"
						ended = True
						break
					elif event.key == pygame.K_DOWN:
						print "Player 1 Down"
						break
					elif event.key == pygame.K_UP:
						pass
					elif event.key == pygame.K_LEFT:
						pass
					elif event.key == pygame.K_RIGHT:
						pass
					elif event.key == pygame.K_s:
						pass
					elif event.key == pygame.K_w:
						pass
					elif event.key == pygame.K_a:
						pass
					elif event.key == pygame.K_d:
						pass

			playerbodies = reduce(operator.add, (player.snake.body for player in self.players))		

			for player in self.players:
				head = player.snake.go()
				if head in self.bord.obstacles or head in playerbodies :
					player.die()
				elif head in self.bord.items.keys() :
					pass # TODO

			self.renderer.render()
		
# vim: ts=2 sw=2
