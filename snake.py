import board

class Snake :

############################# New Snake ###################################
# Input: x, y
# Create a new snake with head at x,y
# Potential to grow as initial
# heading to board's default direction
	def __init__(self, spawn, initial) :
		self.body = [spawn]
		self.growable = initial
		self.dir = board.defaultdir
		self.useddir = self.dir
		
############################# Get Head	###################################
# Input: void
# Get the head
	def gethead (self):
		return self.body[-1]

############################# Go ##########################################
# Input: void
# Return: new head
# Go ahead using dir, if there is potential to grow then  grow
	def go (self):
		head = self.gethead()
		head = board.progress(head, self.dir)
		self.body.append (head)
		if self.growable > 0 :
			self.growable -= 1
		else :
			self.body.pop(0)
		self.useddir = self.dir	
		return head

######################### Reverse ########################################
# Input: void
# Reverse the snake, happens when opponent easts special item
	def reverse (self):
		body.reverse()

######################### Go Up,Down,Right, Left  ########################
# Input: void
# Change direction to up/down/right/left
	def goup (self):
		if self.useddir != board.down :
			self.dir = board.up

	def godown (self):
		if self.useddir != board.up :
			self.dir = board.down

	def goright (self):
		if self.useddir != board.left :
			self.dir = board.right

	def goleft (self):
		if self.useddir != board.right :
			self.dir = board.left

########################### Grow ###############################################
# Input: length
# Add the amount the potential growth
	def grow (self, length) :
		self.growable  += length

# vim: ts=2 sw=2
