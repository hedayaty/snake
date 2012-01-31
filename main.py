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

	# TODO add a menu!
	# TODO put this in combinition with menu into loop

	# number of player, game type, lives, mapname
	while 1:
		gametype = menu.choose (													\
			[("New 1 Single Player", "1p"), 							\
			 ("New 2 Player Game", "2p"),									\
			 ("New 2 Player vs AI", "ai"),								\
			 ("New Network Game as Slave", "slave"),			\
			 ("New Netwrok Game as Master", "master"),		\
			 ("QUIT", None)]);

		if gametype == None : 
			break

		game.init (gametype, 5)
		game.mainloop ()

	pygame.display.quit()
	

if __name__ == "__main__" :
	main ()

# vim: ts=2 sw=2
