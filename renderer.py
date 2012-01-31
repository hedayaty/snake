import pygame, operator, random
from pygame import *
from player import Player
from snake import Snake

import bord, game


def init (isize) :
	global size, bordercolor, screen
	global black, green, blue, pink, maroon

	pink = [ 255, 0, 255] 
	blue = [ 0, 0, 255] 
	maroon = [128, 0, 0]

	size = isize
	screen = pygame.display.set_mode(isize)
	black = [0,0,0]
	green = [0,200,0]
	bordercolor = [160,140,20]
	scorehieght = 16
	size[1] -= scorehieght

def getRect(pixel):
	return Rect(map(operator.mul, pixel, pixelsize), pixelsize)


def updatebord () :
	global bordimage, pixelsize, rfont
	bordimage = pygame.Surface(size)
	pixelsize = map (operator.div, size, bord.dim) 
	rfont = pygame.font.Font(None, int (pixelsize[1]*1.6))
	for pixel in bord.obstacles :
		bordimage.fill (bordercolor, getRect(pixel))

def render ():
	screen.fill(black)
	screen.blit(bordimage, [0]*2)
	# TODO: Render Items
	for player in game.players :
		pixels = player.snake.body
		if player.dead > 0:
			pixels = random.sample (pixels, player.dead * len(pixels) / player.deadtimer)
		for pixel in pixels :
			screen.fill (player.color, getRect(pixel))
				
	for place,item in game.items.iteritems():
		text = rfont.render (item["type"], True, bordercolor)
		screen.blit(text, getRect(place))
	
	margin = 50
	for num,player in enumerate(game.players) :
		text = rfont.render ("{}, Score: {}, Lives: {} "\
		.format(player.name, player.score, player.lives), True, player.color)
		if num == 0:
			loc = margin, size[1] + 1
		else:
			loc = size[0] - margin - text.get_size()[0], size[1] + 1

		screen.blit (text, loc)

	if game.gameover:
		gfont = pygame.font.Font(None,size[1]/3)
		text = gfont.render ("Game Over", True, maroon)
		loc = map(operator.div, map(operator.sub, size, text.get_size()), [2]*2)
		screen.blit (text, loc)
		
	pygame.display.flip()

# vim: ts=2 sw=2
