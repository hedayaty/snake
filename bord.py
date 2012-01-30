
class Bord:
# Define directions
	left = -1 , 0
	right= +1 , 0
	up =    0 , -1
	down =  0 , +1
	defaultdir = right

##################### Init ###################################
# Input: filename
# Read the bord from file and initilize
	def __init__(self, filename):
		# read info from file
		with open (filename) as f: 
			self.name =	f.readline().strip()
			self.dimentions = list(map(int,f.readline().split()))
			self.maxmplayers = int(f.readline())
			self.obstacles = []
			linen = 0
			self.spawn = {}
			for line in f:
				self.obstacles.extend([(i,linen) for i in range(len(line)) if line[i] == "#"] )
				self.spawn.update ({int(line[i]):(i,linen) for i in range(len(line)) if line[i] in map(str,range (1,10))})
				linen += 1

		self.items = {}
		

########################## Add ##################################
# Sudo function used in conjuction with map function 
	def add (self, a, b, c) :
		return (a + b + c) % c;
		
######################### Progress ###############################
# Input: head, dir
# Find the next point on the bord in direction dir, consdering map bounderies
# Wrapping around if reached the bounderies
	def progress (self, head, dir) :
		return tuple(map(self.add, head, dir, self.dimentions))

########################  Get Spawn ######################
# Input: player-number
# Output: location to spawn
	def getspawn (self, number):
# TODO: check if place is available
		return self.spawn[number]

# vim: ts=2 sw=2
