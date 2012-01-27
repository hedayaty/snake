class Snake :

############################# New Snake ###################################
# Input: x, y
# Create a new snake with head at x,y
# Potential to grow as initial
# heading to bord's default direction
	def __init__(self, x, y, initial, bord) :
		self.body = [(x,y)]
		self.growable = initial
		self.bord = bord
		self.dir = bord.defaultdir
		
############################# Get Head	###################################
# Input: void
# Get the head
	def get_head (self):
		return self.body[self.length - 1]

############################# Go ##########################################
# Input: void
# Return: new head
# Go ahead using dir, if there is potential to grow then  grow
	def go (self):
		head = self.get_head()
		head = self.bord.progress(head, self.dir)
		self.body.append (head)
		if self.growable > 0 :
			self.growable -= 1
		else :
			self.body.pop(0)
		
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
		if self.dir != self.bord.down :
			self.dir = self.bord.up

	def godown (self):
		if self.dir != self.bord.up :
			self.dir = self.bord.down

	def goright (self):
		if self.dir != self.bord.left :
			self.dir = self.bord.right

	def goleft (self):
		if self.dir != self.bord.right :
			self.dir = self.bord.left

########################### Grow ###############################################
# Input: length
# Add the amount the potential growth
	def grow (self, length) :
		self.growable  += length

# vim: ts=2 sw=2
