
# Define directions
left = -1 , 0
right= +1 , 0
up =    0 , -1
down =  0 , +1
defaultdir = right

##################### Init ###################################
# Input: filename
# Read the bord from file and initilize
def init(filename):
	# read info from file
	global spawn, obstacles, maxplayers, dim, mapname
	with open (filename) as f: 
		mapname =	f.readline().strip()
		dim = list(map(int,f.readline().split()))
		maxmplayers = int(f.readline())
		obstacles = []
		linen = 0
		spawn = {}
		for line in f:
			obstacles.extend([(i,linen) for i in range(len(line)) if line[i] == "#"] )
			spawn.update ({int(line[i]):(i,linen) for i in range(len(line)) if line[i] in map(str,range (1,10))})
			linen += 1


########################## Add ##################################
# Sudo function used in conjuction with map function 
def _add (a, b, c) :
	return (a + b + c) % c;
		
######################### Progress ###############################
# Input: head, dir
# Find the next point on the bord in direction dir, consdering map bounderies
# Wrapping around if reached the bounderies
def progress (head, dir) :
	return tuple(map(_add, head, dir, dim))

# vim: ts=2 sw=2
