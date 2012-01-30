import pygame, operator
from pygame import *
from bord import Bord
from player import Player
from snake import Snake


def init (isize) :
	global size, black, bordercolor, screen

	size = isize
	screen = pygame.display.set_mode(size)
	black = 0,0,0
	bordercolor =160,140,20

def getRect(pixel):
	return Rect(map(operator.mul, pixel, pixelsize), pixelsize)


def updatebord (ibord) :
	global bordimage, pixelsize, bord
	bord = ibord
	bordimage = pygame.Surface(size)
	pixelsize = map (operator.div, size, bord.dimentions) 
	for pixel in bord.obstacles :
		bordimage.fill (bordercolor, getRect(pixel))

def render (players):
	screen.fill(black)
	screen.blit(bordimage, [0]*2)
	# TODO: Render Items
	for player in players :
		for pixel in player.snake.body :
			screen.fill (player.color, getRect(pixel))
	pygame.display.flip()

# vim: ts=2 sw=2
