#!/usr/bin/python

import sys, pygame
import operator
from pprint import pprint
from pygame import *

import game,renderer, menu

def main():
	
	pygame.init()

	size = width, height = [640,480+16]
	renderer.init(size)
	pygame.display.set_caption("snake")
	menu.init()
	
	
	# number of player, game type, lives, mapname
	while 1:	
		gametype = menu.choose ("",																			\
		[{ "label" : "Single Player", "value": "1p"}, 									\
		 { "label" : "Multi Players Game", "value": "multi"},						\
		 { "label" : "Join a Network Game", "value" : "join"},					\
		 { "label" : "QUIT", "value": None}])	

		if gametype == None : 
			break
		
		if game.init (gametype):
			game.mainloop ()

	pygame.display.quit()
	

if __name__ == "__main__" :
	main ()

# vim: ts=2 sw=2
