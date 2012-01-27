class Player:
	# Initilize
	def __init__(self, board, name, color, lives):
		self.bord = bord
		self.snake = Snake(board)
		self.lives = lives

	def die (self):
		self.lives -= 1
		self.snake = Snake(bord)
		return self.lives == 0
# vim: ts=2 sw=2
