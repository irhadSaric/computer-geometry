from point import *
from vector import Vector
from simplePoly import *

a = [(0, 0), (3, 0), (-1, -3), (-1, 3), [-2, 3], [2, 5], [-1, 1], [-4, 1], [-5, -2]]

"""if Point.orientation(Point(*a[0]), Point(*a[1]), Point(*a[2])) == 1:
    print("Counter clockwise")
elif Point.orientation(Point(*a[0]), Point(*a[1]), Point(*a[2])) == 0:
    print("Clockwise")
else:
    print("Collinear")

if Vector.do_intersect(Vector(Point(*a[0]), Point(*a[1])), Vector(Point(*a[2]), Point(*a[3]))):
    print("Do intersect")
else:
    print("Don't intersect")"""

print(simplePoly(a))
