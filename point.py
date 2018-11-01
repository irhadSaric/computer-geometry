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
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __gt__(self, other: 'Point'):
        return self.x > other.x or (self.x == other.x and self.y > other.y)