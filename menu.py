import operator, pygame, itertools

import renderer

############################### Init ###################################
# Input: void
# Initilize the module for usage
def init ():
	global screen, size, triangle, black, textcolor, selcolor
	global clock, margin, rows, height, font, titlesize
	global triangletop, triangledown
	global inputkeys

	screen = renderer.screen
	size = renderer.size
	triangle = [(0,0), (0,32), (16,16)]
	black = renderer.black
	textcolor = [255, 127, 0] # Orange
	selcolor = [255,255,255] # White
	clock = pygame.time.Clock()
	margin = size[1] / 8
	rows = 6
	height = (size[1] - 2 * margin) / rows 
	titlesize = height / 2
	triangletop = [	(size[0] / 2 - margin * 2,  margin * 7 / 8 + titlesize),	\
									(size[0] / 2,  margin * 5 / 8 + titlesize),								\
									(size[0] / 2 + margin * 2,  margin * 7 / 8 + titlesize)]
	
	triangledown = [(size[0] / 2 - margin * 2,  size[1] - margin * 7 / 8 + titlesize),	\
									(size[0] / 2,  size[1] - margin * 5 / 8 + titlesize),								\
									(size[0] / 2 + margin * 2,  size[1] - margin * 7 / 8 + titlesize)]
	font = pygame.font.Font(None, height)
	inputkeys = range(pygame.K_a,pygame.K_z + 1) + \
							range(pygame.K_0,pygame.K_9+1) + [pygame.K_SPACE]

############################ Render ######################################
# Input: items
# Renders the menu on screen
def render (items, values=None) :
	screen.fill(black)
	pos = margin - height
	label = font.render (menutitle , True, textcolor)
	width = label.get_size()[0]
	screen.blit (label, ((size[0] - width) / 2, pos + margin / 4))
	pos += titlesize

	for item in items[window["top"]:window["down"]] :
		pos += height
		if item.has_key("name"):
			name = item["name"]
			if item.has_key("options"): # Color/Combo
				val = values[name]["value"]
				text = values[name]["label"]
			else:
				text = values[name] # Entry
		else:
			text = item["label"] # Normal Menu Item

		# Addd description if available
		if item.has_key("description"):
			text = item["description"] + text

		if text == "color":
			width = size[0] / 5
			screen.fill (val, pygame.Rect((size[0] - width) / 2, pos, width, height / 2 ))
		else:
			color = selcolor if item == items[sel] else textcolor
			label = font.render (text , True, color)
			width = label.get_size()[0]
			screen.blit (label, ((size[0] - width) / 2, pos))

		# Also render triangle around selected item
		if item == items[sel]:
			p1 = [ ((size[0] - width) / 2 - 10 - x, pos + y) for x,y in triangle]
			p2 = [ ((size[0] + width) / 2 + 10 + x, pos + y) for x,y in triangle]
			pygame.draw.polygon(screen, textcolor, p1)
			pygame.draw.polygon(screen, textcolor, p2)

	if window["top"] > 0:
		pygame.draw.polygon(screen, textcolor, triangletop)
	if window["down"] < len(items):
		pygame.draw.polygon(screen, textcolor, triangledown)

	pygame.display.flip()

################################## Choose ##################################
# Input: items [label, value]
# Output: chosen item ["value"]
def choose (title, items):
	global window, sel, menutitle
	menutitle = title
	window = { "top" : 0, "down" : min(rows, len(items)) }
	sel = 0
	selected = False
	while not selected:
		clock.tick(10)
		render (items)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				return None
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return None
				elif event.key == pygame.K_DOWN:
					if sel < len(items) - 1 :
						sel += 1
						if sel == window["down"]:
							window["top"] += 1
							window["down"] += 1
	
				elif event.key == pygame.K_UP:
					if sel > 0 :
						sel -= 1
						if sel < window["top"]:
							window["top"] -= 1
							window["down"] -= 1

				elif event.key in [ pygame.K_RETURN, pygame.K_KP_ENTER ] :
					selected = True

	return items[sel]["value"]
						
###################################### Select ##############################
# Input: items
# Selects items
# item[name, label]: entry
# item[name, options*[label,value]]: combo
# item[name, options*[label="color",value]]: color

def select(title, items):
	global window, sel, menutitle
	menutitle = title
	values = {}
	iterators = {}
	pos = {}
	for item in items:
		name = item["name"]
		if item.has_key("label"):
			values[name] = item["label"]
			pos[name] = len(item["label"])
		else:
			iterators[name] = itertools.cycle(item["options"])
			if item.has_key ("default") :
				default = item["default"]
				if [ option  for option in item["options"] if default == option["value"] ]:
					while 1:
						values[name] = iterators[name].next()
						if values[name]["value"] == default:
							break
				else:
					values[name] = iterators[name].next()
			else:
				values[name] = iterators[name].next()
	window = { "top" : 0, "down" : min(rows, len(items)) }
	sel = 0

	selected = False
	while not selected:
		clock.tick(10)
		render (items, values)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				return None
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return None 
				elif event.key in [ pygame.K_RETURN, pygame.K_KP_ENTER] :
					selected = True
				elif event.key == pygame.K_DOWN:
					if sel < len(items) - 1 :
						sel += 1
						if sel == window["down"]:
							window["top"] += 1
							window["down"] += 1
	
				elif event.key == pygame.K_UP:
					if sel > 0 :
						sel -= 1
						if sel < window["top"]:
							window["top"] -= 1
							window["down"] -= 1

				elif event.key == pygame.K_RIGHT:
					item = items[sel]
					name=items[sel]["name"]
					if item.has_key("label") :
						if pos[name] < len(values[name]):
							pos[name] += 1
					else:
						values[name] = iterators[name].next()
				elif event.key == pygame.K_LEFT:
					item = items[sel]
					name=items[sel]["name"]
					if item.has_key("label") :
						if pos[name] > 0:
							pos[name] -= 1
					else:
						for i in range(len(item["options"]) - 1) :
							values[name] = iterators[name].next()
				elif event.key == pygame.K_BACKSPACE :
					item = items[sel]
					name=items[sel]["name"]
					if item.has_key("label") :
						if pos[name] > 0:
							old = values[name]
							values[name] = old[0:pos[name] - 1] + old[pos[name]: len(old)]
							pos[name] -= 1
				elif event.key in inputkeys :
					item = items[sel]
					name=items[sel]["name"]
					if item.has_key("label") :
						old = values[name]
					 	key	= event.unicode
						values[name] = old[0:pos[name]] + key  + old[pos[name]: len(old)]
						pos[name] += 1

	return values

# vim: ts=2 sw=2
