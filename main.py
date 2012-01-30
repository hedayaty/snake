#!/usr/bin/python

import sys, pygame
import operator
from pprint import pprint
from pygame import *

from snake import Snake
from bord import Bord
from game import Game
from player import Player
from renderer import Renderer

def main():
	
	pygame.init()

	size = width, height = 640,480
	renderer = Renderer (size)
#  pygame.display.set_caption('snake')

	# TODO add a menu!
	# TODO put this in combinition with menu into loop

	# renderer, number of player, game type, lives, mapname
	game = Game(renderer, 2, "2P", 5, "simple")

	game.mainloop ()
	

if __name__ == "__main__" :
	main ()

# vim: ts=2 sw=2
