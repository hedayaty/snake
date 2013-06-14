import socket, pygame

import player, renderer

# Write snake reverse in cel phone you get 35267!
################## Start Server #########################
# Input: port#
# Start listening on the port, waiting for other players
def startserver (port=35267):
	global listenning
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind((socket.gethostname(), port))

####################### Wait for  ########################
# Input: player
# Output: None on cancel, network error, or timeout; otherwise, anything non-None!
# Wait for player to connect from network
# Store client socket info in player
def waitfor (player):
#	clientsocket,addr = serversocket.listen(1)
	screen = renderer.screen	
	size = renderer.size
	black = renderer.black
	clock = pygame.time.Clock()
	textcolor = [255, 127, 0] # Orange
	font = pygame.font.Font(None, size[1] / 10 )
	while 1:
		clock.tick(10)
		screen.fill(black)
		text = font.render ("Waiting for " + player.name + " ...", True, textcolor)
		screen.blit(text, map(lambda x,y: (x - y) / 2, size, text.get_size()))
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				return None
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return None
		pygame.display.flip()

########################## Get Key ############################
# Input: player
# Check players network socket if player has sent any key
def getkey(player):
	pass

######################## Send Info #############################
# Input: player, players, items
# Send players and items to player so he can render the screen
def sendinfo (player, players, items):
	pass

####################### Send bord ########################
# Input: player, players, 
# Send bord 
def sendbordi (player, dim, obstacles):
	pass
	
	
# vim: ts=2 sw=2
