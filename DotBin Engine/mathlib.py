import numpy as np
import math


def smoothstep(t):
	return t * t * (3.0 - 2.0 * t)


def lerp(t, a, b):
	return a + t * (b - a)


class Vector2D:
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y


	def set_xy(self, x, y):
		self.x = x
		self.y = y


	def get_xy(self):
		return self.x, self.y


	def set_x(self, x):
		self.x = x


	def set_y(self, y):
		self.y = y

	def __add__(self, other):
		if isinstance(other, Vector2D):
			return self.x + other.x, self.y + other.y
		else:
			raise TypeError("Other must be of type Vector2D")


	def __radd__(self, other):
		return self.__add__(other)


	def __sub__(self, other):
		if isinstance(other, Vector2D):
			return self.x - other.x, self.y - other.y
		else:
			raise TypeError("Other must be of type Vector2D")


	def __rsub__(self, other):
		return self.__sub__(other)


	def __mul__(self, other):
		if isinstance(other, Vector2D):
			return self.x * other.x, self.y * other.y
		else:
			raise TypeError("Other must be of type Vector2D")
	

	def __rmul__(self, other):
		return self.__mul__(other)


	def __div__(self, other):
		if isinstance(other, Vector2D):
			return self.x / other.x, self.y / other.y
		else:
			raise TypeError("Other must be of type Vector2D")


	def __rdiv__(self, other):
		return self.__div__(other)


	def __mod__(self, other):
		if isinstance(other, Vector2D):
			return self.x % other.x, self.y % other.y
		else:
			raise TypeError("Other must be of type Vector2D")


	def __eq__(self, other):
		if isinstance(other, Vector2D):
			if self.x == other.x and self.y == other.y:
				return True
			else:
				return False
		else:
			raise TypeError("Other must be of type Vector2D")


	def __neg__(self):
		return Vector2D(-self.x, -self.y)


	def __getitem__(self, index):
		if index > 1:
			raise IndexError("Index must be less than 2")

		if index == 0:
			return self.x
		else:
			return self.y

	
	def __setitem__(self, index, value):
		if index > 1:
			raise IndexError("Index must be less than 2")
		if index == 0:
			self.x = value
		else:
			self.y = value


	def __len__(self):
		return 2


	def copy(self):
		new_vec = Vector2D
		new_vec.x = self.x
		new_vec.y = self.y
		return new_vec


	def length(self):
		return np.sqrt((self.x * self.x) + (self.y * self.y))


	def normalize(self):
		length = self.length()
		if length > 0:
			self.x /= length
			self.y /= length
		else:
			print("Length 0, cannot normalize")


	def normalize_copy(self):
		vec = self.copy()
		vec.normalize()
		return vec


	def distance(vec1, vec2):
		"""Calculate the distance between two Vectors"""
		#dist_vec = Vector2D()
		if isinstance(vec1, Vector2D)   \
		and isinstance(vec2, Vector2D):
			dist_vec = vec2 - vec1
			print dist_vec
			return np.sqrt((dist_vec[0] * dist_vec[0]) + (dist_vec[1] * dist_vec[1]))
		else:
			raise TypeError("vec1 and vec2 must be Vector2D's")

	def dot(vec1, vec2):
		"""Calculate the dot product between two Vectors"""
		if isinstance(vec1, Vector2D)   \
		and isinstance(vec2, Vector2D):
			return ( (vec1.x * vec2.x) + (vec1.y * vec2.y) )
		else:
			raise TypeError("vec1 and vec2 must be Vector2D's")

	def angle(vec1, vec2):
		"""Calculate the angle between two Vector2D's"""
		dotp = Vector2D.dot(vec1, vec2)
		mag1 = vec1.length()
		mag2 = vec2.length()
		result = dotp / (mag1 * mag2)
		return math.acos(result)

	def lerp(vec1, vec2, time):
		"""Lerp between vec1 to vec2 based on time. Time is clamped between 0 and 1."""
		if isinstance(vec1, Vector2D)    \
		and isinstance(vec2, Vector2D):
			#Clamp the time value into the 0-1 range.
			if time < 0:
				time = 0
			elif time > 1:
				time = 1

			x_lerp = vec1[0] + time * (vec2[0] - vec1[0])
			y_lerp = vec1[1] + time * (vec2[1] - vec1[1])
			return Vector2D(x_lerp, y_lerp)
		else:
			raise TypeError("Objects must be of type Vector2D")


	def from_polar(degrees, magnitude):
		"""Convert polar coordinates to Carteasian Coordinates"""
		vec = Vector2D()
		vec.x = np.cos(math.radians(degrees)) * magnitude

		#Negate because y in screen coordinates points down, oppisite from what is
		#expected in traditional mathematics.
		vec.y = -np.sin(math.radians(degrees)) * magnitude
		return vec


	def component_mul(vec1, vec2):
		"""Multiply the components of the vectors and return the result."""
		new_vec = Vector2D()
		new_vec.x = vec1.x * vec2.x
		new_vec.y = vec1.y * vec2.y
		return new_vec


	def component_div(vec1, vec2):
		"""Divide the components of the vectors and return the result."""
		new_vec = Vector2D()
		new_vec.x = vec1.x / vec2.x
		new_vec.y = vec1.y / vec2.y
		return new_vec

	
	distance = staticmethod(distance)
	dot = staticmethod(dot)
	lerp = staticmethod(lerp)
	from_polar = staticmethod(from_polar)
	component_mul = staticmethod(component_mul)
	component_div = staticmethod(component_div)

	
class Ray(object):
	def __init__(self, origin=Vector2D, direction=Vector2D):
		self.origin = origin
		self.direction = direction
		self.direction.normalize()

	def get_point(self, scalar_val):
		"""Get a point along the ray."""
		return scalar_val * self.direction + self.origin







