from constant import *



class Tile:
	def __init__(self, image, x, y):
		if isinstaance(pg.Surface, image):
		self.image = image

		self.pos = x * TILESIZE, y * TILESIZE