
# Define directions
left = -1 , 0
right= +1 , 0
up =    0 , -1
down =  0 , +1
dirs = [left, right, up, down]
defaultdir = right

##################### Init ###################################
# Input: filename
# Read the board from file and initilize
def init(filename):
	# read info from file
	global  obstacles, dim, mapname
	with open (filename) as f: 
		mapname =	f.readline().strip()
		dim = list(map(int,f.readline().split()))
		obstacles = []
		linen = 0
		for line in f:
			obstacles.extend([(i,linen) for i in range(len(line)) if line[i] == "#"] )
			linen += 1

########################## Add ##################################
# Sudo function used in conjuction with map function 
def _add (a, b, c) :
	return (a + b + c) % c;
		
######################### Progress ###############################
# Input: head, dir
# Find the next point on the board in direction dir, consdering map bounderies
# Wrapping around if reached the bounderies
def progress (head, dir) :
	return tuple(map(_add, head, dir, dim))

# vim: ts=2 sw=2
