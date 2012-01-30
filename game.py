import sys,pygame,operator,random
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
		self.otheritemtypes = ["R", " ", "P"]
		renderer.updatebord(self.bord)
	
	def place (self, playerbodies, type):
		blocked = playerbodies + \
							self.bord.obstacles +\
							self.bord.items.keys()
		dim = self.bord.dimentions
		place = blocked[0]
		while place in blocked:
			place = random.randint(0,dim[0]-1),random.randint(0,dim[1]-1)

		self.bord.items[place] = {"type": type, "timer":300}
		return place

	def mainloop (self):
		digit = 1
		clock = pygame.time.Clock()

		# TODO: Trow items on the bord!
		playerbodies = reduce(operator.add, (player.snake.body for player in self.players))		
		digplace = self.place(playerbodies, str(digit))
		wait = False

		while 1:
			clock.tick(10)

			# Render the screen
			renderer.render(self.players, self.bord.items)

			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					return
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return
					for player in self.players:
						player.usekey (event.key)
						
			if wait:
				continue
			#TODO: for network game as master, also process keys from client
			#TODO: for network game as slave, also send keys to server

	
			for player in self.players:
				head = player.go()
				# Check if hit the wall or ther players
				if head in self.bord.obstacles or head in playerbodies : 
					if digit > 5:
						digit -= 4
					else:
						digit = 1
					self.bord.items[digplace]["type"] = str(digit)
					if player.die() :
						wait = True
						break

				# Check if hit any items
				elif head in self.bord.items.keys() :
					# TODO: Assumed items are only numbers
					del self.bord.items[head]
					player.score += 10 * digit
					player.snake.grow(digit)
					digit += 1
					if digit == 10:
						wait = True
						break
					else:
						digplace = self.place (playerbodies, str(digit))
				

			# keep track of player bodies as obstacles as well
			playerbodies = reduce(operator.add, (player.snake.body for player in self.players))		

			# Check for timer exppirations
			for place in self.bord.items.keys() :
				self.bord.items[place]["timer"] -= 1
				if self.bord.items[place]["timer"] == 0 :
					type = self.bord.items[place]["type"]
					del self.bord.items[place]
					if type in self.otheritemtypes :
						self.place (playerbodies, random.choice(self.otheritemtypes))
					else: # It is number, put the same number somewhere else on the bord
						digplace = self.place (playerbodies, type)

				
		
# vim: ts=2 sw=2
