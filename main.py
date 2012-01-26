#!/usr/bin/python

import sys, pygame
from pprint import pprint
from pygame import *

from snake import Snake
from bord import Bord
from game import Game
from player import Player


def main():
	pygame.init()

	size = width, height = 640,480
	black = 0,0,0
	screen = pygame.display.set_mode(size)

	bord = Bord("maps/simple.sn");
	pprint (vars(bord))
#	json.dumps(bord)

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		screen.fill(black)
	#	screen.blit(ball, ballrect)
		pygame.display.flip()

if __name__ == "__main__" :
	main ()

# vim: ts=2 sw=2
