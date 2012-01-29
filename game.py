class Game:
	def __init(self, nplayers, type, lives, mapname):
		# TODO Select Game Type
		# - 1P
		# - 2P
		# - 1P vs AI
		# - 1p vs Network (Master)
		# - Network vs 1p (Slave)
		# TODO Select Bord if needed
		# in case of slave network game this is not needed
		# Get the name of the player + color

		self.bord = Bord("maps"+ mapname + ".sn")

		# TODO: Pick name/color
		name1 = "Player 1"
		color1 = [ 0, 0, 255] # Blue
		self.players = [Player(bord, name1, color1, lives)]

		if nplayer == 2:
			name2 = "Player 2"
			color2 = [ 255, 0, 255] # Red
			self.players.append(Player(bord, name2, color2, lives))

		self.type == type
	

	def main_loop (self):

		ended = False
		# TODO: Trow items on the bord!

		while ended == False:
			clock.tick(10)
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						ended = False
						break
					elif event.key == pygame.K_DOWN:
						pass
					elif event.key == pygame.K_UP:
						pass
					elif event.key == pygame.K_LEFT:
						pass
					elif event.key == pygame.K_RIGHT:
						pass
					elif event.key == pygame.K_s:
						pass
					elif event.key == pygame.K_w:
						pass
					elif event.key == pygame.K_a:
						pass
					elif event.key == pygame.k_d:
						pass
		reduce(operator.add, (player.snake.body for player in players))		

		for player in self.players:
			head = player.snake.go()
			if head in bord.obstacles or head in playerbodies :
				player.die()
			elif head in bord.items() :
				pass # TODO
		
# vim: ts=2 sw=2
