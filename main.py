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

	clock = pygame.time.Clock()

	size = width, height = 640,480
	screen = pygame.display.set_mode(size)
#  pygame.display.set_caption('snake')
	Renderer.size = size
	Rednerer.screen = screen

	# TODO add a menu!
	# TODO put this in combinition with menu into loop

	# number of player, game type, lives, mapname
	game = Game(2, "2P", 5, "simple")
	

if __name__ == "__main__" :
	main ()

# vim: ts=2 sw=2
