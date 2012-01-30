import pygame, operator
from pygame import *
from bord import Bord
from player import Player
from snake import Snake


def init (isize) :
	global size, bordercolor, screen
	global black, green

	size = isize
	screen = pygame.display.set_mode(isize)
	black = [0,0,0]
	green = [0,200,0]
	bordercolor = [160,140,20]
	scorehieght = 16
	size[1] -= scorehieght

def getRect(pixel):
	return Rect(map(operator.mul, pixel, pixelsize), pixelsize)


def updatebord (ibord) :
	global bordimage, pixelsize, bord, rfont
	bord = ibord
	bordimage = pygame.Surface(size)
	pixelsize = map (operator.div, size, bord.dimentions) 
	rfont = pygame.font.Font(None,pixelsize[1]*2)
	for pixel in bord.obstacles :
		bordimage.fill (bordercolor, getRect(pixel))

def render (players, items):
	screen.fill(black)
	screen.blit(bordimage, [0]*2)
	# TODO: Render Items
	for player in players :
		for pixel in player.snake.body :
			if player.dead == 0:
				screen.fill (player.color, getRect(pixel))
			else:
				color = map (lambda x: x*player.dead/6, player.color)
				screen.fill (color, getRect(pixel))
				
	for place,item in items.iteritems():
		text = rfont.render (item["type"], True, bordercolor)
		screen.blit(text, getRect(place))
	
	margin = 50
	for player in players :
		text = rfont.render ("Player: {}, Score: {}, Lives: {} "\
		.format(player.number, player.score, player.lives), True, player.color)
		if player.number == 1 :
			screen.blit (text, Rect((margin, size[1] + 1), (0,0)))
		else :
			screen.blit (text, Rect((size[0] - margin - text.get_size()[0], size[1] + 1), (0,0)))
		
		
	pygame.display.flip()

# vim: ts=2 sw=2
