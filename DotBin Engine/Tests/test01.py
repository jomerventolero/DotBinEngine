from mathlib import *

v1 = Vector2D(5,5)
v2 = Vector2D(1,1)

dist = Vector2D.distance(v1, v2)
print dist
dot = Vector2D.dot(v1, v2)
print dot
angle = Vector2D.angle(v1, v2)
lerp = Vector2D.lerp(v1, v2, 3)
print lerp
from_polar = Vector2D.from_polar(45, 1)
print from_polar
mul = Vector2D.component_mul(v1, v2)
print mul
div = Vector2D.component_div(v1, v2)

