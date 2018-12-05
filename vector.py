from point import *

class Vector:
    def __init__(self, head: 'Point', tail: 'Point'):
        self.head = head
        self.tail = tail

    def magnitude(self):
        return self.head.euclidean_distance(self.tail)

    def dot(self, v: 'Vector') -> float:
        prod_x = (self.tail.x - self.head.x) * (v.tail.x - v.head.x)
        prod_y = (self.tail.y - self.head.y) * (v.tail.y - v.head.y)

        return prod_x + prod_y

    @staticmethod
    def do_intersect(s_1: 'Vector', s_2: 'Vector') -> bool:

        # orientation of the (self.tail, self.head, s_2.tail) triangle
        s_1_orientation_tail = Point.orientation(s_1.tail, s_1.head, s_2.tail)

        # orientation of the (self.tail, self.head, s_2.head) triangle
        s_1_orientation_head = Point.orientation(s_1.tail, s_1.head, s_2.head)

        # orientation of the (s_2.tail, s_2.head, self.tail) triangle
        s_2_orientation_tail = Point.orientation(s_2.tail, s_2.head, s_1.tail)

        # orientation of the (s_2.tail, s_2.head, self.head) triangle
        s_2_orientation_head = Point.orientation(s_2.tail, s_2.head, s_1.head)

        # general case
        if s_1_orientation_tail != s_1_orientation_head and s_2_orientation_tail != s_2_orientation_head:
            return True

        # collinear case
        if s_1_orientation_tail == 0 and s_1_orientation_head == 0 and s_2_orientation_tail == 0 and s_2_orientation_head == 0:

            if s_1.tail.between(s_2.head, s_2.tail) or s_1.head.between(s_2.head, s_2.tail) \
                    or s_2.tail.between(s_1.head, s_1.tail) or s_2.head.between(s_1.head, s_1.tail):
                return True
        return False