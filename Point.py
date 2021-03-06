from math import sqrt
from sys import maxsize

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):

        self.x = x
        self.y = y

    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __rmul__(self, other: int):
        return self.__mul(other)

    def __mul__(self, other: float):
        return self.__mul(other)

    def __mul(self, other: float):
        return Point(other * self.x, other * self.y)

    def __truediv__(self, other):
        return self.__div(other)

    def __div(self, other: float):

        if other == 0.0:
            return Point(maxsize, maxsize)

        else:
            return Point(self.x / other, self.y / other)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other: 'Point'):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other: 'Point'):
        return not self.__eq__(other)

    def __lt__(self, other: 'Point'):
        return self.x < other.x or (self.x == other.x and self.y > other.y)

    def __gt__(self, other: 'Point'):
        return self.x > other.x or (self.x == other.x and self.y > other.y)

    def __hash__(self):
        from Segment import Segment
        s = Segment(Point(0, 0), self)
        k = s.get_coef()
        string = str(k + self.euclidean_distance(Point(0, 0)) + self.x + self.y)
        i = len(string)
        rez = 0
        for char in string:
            rez += pow(10, i)+ord(char)
            i -= 1
        return rez

    def euclidean_distance(self, b:'Point') -> float:
        return sqrt((b.x - self.x)**2 + (b.y - self.y)**2)

    def between(self, p1: 'Point', p2: 'Point'):
        return min(p1.x, p2.x) <= self.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= self.y <= max(p1.y, p2.y)

    @staticmethod
    def obim(a: 'Point', b:'Point', c:'Point') -> float:
        sum = 0.0
        sum += Point.euclidean_distance(a, b) + Point.euclidean_distance(b,c) + Point.euclidean_distance(c, a)
        return sum

    @staticmethod
    def orientation2D(a: 'Point', b: 'Point', c: 'Point'):
        p1: Point = b - a
        p2: Point = c - a

        crossProduct = p1.x * p2.y - p1.y * p2.x

        if crossProduct > 0:
            return 1 # Left orientation, counter clockwise direction
        elif crossProduct < 0:
            return 0 # Right orientation, clockwise direction
        else:
            return -1 # Colinear points

class EventPoint(Point):
    def __init__(self, event_type: str, point: 'Point', segment_identifier):
        super().__init__(point.x, point.y)
        self.event_type = event_type
        self.segment_identifier = segment_identifier