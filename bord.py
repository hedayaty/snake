
class Bord:
# Define directions
	left = -1,0
	right= +1,0
	up = -1,0
	down = +1,0
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
				self.obstacles.extend([(linen,i) for i in range(len(line)) if line[i] == "#"] )
				self.spawn.update ({int(line[i]):(linen,i) for i in range(len(line)) if line[i] in map(str,range (1,10))})
				linen += 1

		self.items = []
		

########################## Add ##################################
# Sudo function used in conjuction with map function 
	def add (a, b, c) :
		return (a + b + c) % c;
		
######################### Progress ###############################
# Input: head, dir
# Find the next point on the bord in direction dir, consdering map bounderies
# Wrapping around if reached the bounderies
	def progress (self, head, dir) :
		return list(map(head, dir, self.dimentions))

# vim: ts=2 sw=2
