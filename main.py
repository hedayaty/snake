#!/usr/bin/python

#import sys, pygame
from pprint import pprint
#from pygame import *

from snake import Snake
from bord import Bord
from game import Game
from player import Player


def main():
	bord = Bord("maps/simple.sn");
	pprint (vars(bord))

	quit()
	
	pygame.init()

	clock = pygame.time.Clock()

	size = width, height = 640,480
	black = 0,0,0
	screen = pygame.display.set_mode(size)


		screen.fill(black)
	#	screen.blit(ball, ballrect)
		pygame.display.flip()

if __name__ == "__main__" :
	main ()

# vim: ts=2 sw=2
