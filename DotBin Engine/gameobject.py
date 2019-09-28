''' Game Object Wrapper for DotBin Game Engine '''

class GameObject(Vector2D):
	def __init__(self, name, position=Vector2D()):
		super(Vector2D, self).__init__()
		self.name = name
		self.x = position[0]
		self.y = position[1]