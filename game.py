class Game:
	def __init(self):
		# TODO Select Game Type
		# - 1P
		# - 2P
		# - 1P vs AI
		# - 1p vs Network (Master)
		# - Network vs 1p (Slave)
		# TODO Select Bord if needed
		# in case of slave network game this is not needed
		# Get the name of the player + color
		bord = bord("maps/TODO")
		self.players = [player("Player 1", bord), player("Player 2", bord)]
		


# vim: ts=2 sw=2
