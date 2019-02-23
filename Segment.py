from copy import deepcopy

from Point import *
from math import sqrt
import random


class Segment:
    def __init__(self, start: 'Point', end: 'Point'):
        self.start = start
        self.end = end
        self.currenty = start.y

    def __repr__(self):
        return '({}, {}, {})'.format(self.start, self.end, self.currenty)

    def __lt__(self, other):
        return self.currenty < other.currenty or (self.currenty == other.currenty and self.start.y > other.start.y)

    def get_coef(self):
        from math import atan2
        theta = atan2((self.end.y - self.start.y), (self.end.x - self.start.x))
        return theta

    def get_random_point(self, lower: int, upper: int, flight_type: str) -> 'Point':
        a = self.end.y - self.start.y
        b = self.start.x - self.end.x
        c = a * self.start.x + b * self.start.y

        x = random.uniform(self.start.x, self.end.x)
        if b == 0:
            y = random.uniform(self.start.y, self.end.y)
        else:
            y = c / b - a / b * x

        if flight_type == "external":
            z = random.randint(upper, upper+100)
        else:
            z = random.randint(lower, upper)

        return Point(x, y, z)

    @staticmethod
    def do_intersect(s_1: 'Segment', s_2: 'Segment') -> bool:

        # orientation of the (self.end, self.start, s_2.end) triangle
        s_1_orientation_end = Point.orientation2D(s_1.end, s_1.start, s_2.end)

        # orientation of the (self.end, self.start, s_2.start) triangle
        s_1_orientation_start = Point.orientation2D(s_1.end, s_1.start, s_2.start)

        # orientation of the (s_2.end, s_2.start, self.end) triangle
        s_2_orientation_end = Point.orientation2D(s_2.end, s_2.start, s_1.end)

        # orientation of the (s_2.end, s_2.start, self.start) triangle
        s_2_orientation_start = Point.orientation2D(s_2.end, s_2.start, s_1.start)

        # general case
        if s_1_orientation_end != s_1_orientation_start and s_2_orientation_end != s_2_orientation_start:
            return True

        # collinear case
        if s_1_orientation_end == 0 and s_1_orientation_start == 0 and s_2_orientation_end == 0 and s_2_orientation_start == 0:

            if s_1.end.between2D(s_2.start, s_2.end) or s_1.start.between2D(s_2.start, s_2.end) \
                    or s_2.end.between2D(s_1.start, s_1.end) or s_2.start.between2D(s_1.start, s_1.end):
                return True
        return False

    @staticmethod
    def point_of_intersection(s_1: 'Segment', s_2: 'Segment') -> Point:
        x12 = s_1.start.x - s_1.end.x
        x34 = s_2.start.x - s_2.end.x
        y12 = s_1.start.y - s_1.end.y
        y34 = s_2.start.y - s_2.end.y

        c = x12 * y34 - y12 * x34

        a = s_1.start.x * s_1.end.y - s_1.start.y * s_1.end.x
        b = s_2.start.x * s_2.end.y - s_2.start.y * s_2.end.x

        x = (a * x34 - b * x12) / c
        y = (a * y34 - b * y12) / c

        return Point(x, y)
