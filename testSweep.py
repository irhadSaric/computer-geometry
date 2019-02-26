from queue import PriorityQueue
from Point import *
from Segment import Segment
from avlpokusaj import AVLTree

def get_intersections(segments: list):
    PQ = PriorityQueue()
    tree = AVLTree()
    visited = dict()
    set_of_intersection_points = set()
    for segment in segments:
        PQ.put(EventPoint("start", segment.start, segment))
        PQ.put(EventPoint("end", segment.end, segment))

    while not PQ.empty():
        event_point = PQ.get()
        visited[Point(event_point.x, event_point.y)] = 1

        if event_point.event_type == "start":
            current_segment = event_point.segment_identifier
            tree.insert(current_segment)
            segment_above = tree.get_succ(tree.find(current_segment).key)
            segment_below = tree.get_prev(tree.find(current_segment).key)

            if segment_above != None:
                segment_above = tree.get_succ(tree.find(current_segment).key).key
                if Segment.do_intersect(current_segment, segment_above):
                    try:
                        if not visited[Segment.point_of_intersection(current_segment, segment_above)]:
                            PQ.put(EventPoint("intersection", Segment.point_of_intersection(current_segment, segment_above),
                                      [segment_above, current_segment]))
                    except KeyError:
                        PQ.put(EventPoint("intersection", Segment.point_of_intersection(current_segment, segment_above),
                                          [segment_above, current_segment]))

            if segment_below != None:
                segment_below = tree.get_prev(tree.find(current_segment).key).key
                if Segment.do_intersect(current_segment, segment_below):
                    try:
                        if not visited[Segment.point_of_intersection(current_segment, segment_below)]:
                            PQ.put(EventPoint("intersection", Segment.point_of_intersection(current_segment, segment_below),
                                      [current_segment, segment_below]))
                    except KeyError:
                        PQ.put(EventPoint("intersection", Segment.point_of_intersection(current_segment, segment_below),
                                          [current_segment, segment_below]))
        elif event_point.event_type == "end":
            current_segment = event_point.segment_identifier
            segment_above = tree.get_succ(tree.find(current_segment).key)
            segment_below = tree.get_prev(tree.find(current_segment).key)

            if segment_above != None:
                segment_above = tree.get_succ(tree.find(current_segment).key).key
            if segment_below != None:
                segment_below = tree.get_prev(tree.find(current_segment).key).key

            tree.remove(current_segment)

            if segment_above != None and segment_below != None and Segment.do_intersect(segment_above, segment_below):
                try:
                    if not visited[Segment.point_of_intersection(segment_above, segment_below)]:
                        PQ.put(EventPoint("intersection", Segment.point_of_intersection(segment_above, segment_below),
                                          [segment_above, segment_below]))
                except KeyError:
                    PQ.put(EventPoint("intersection", Segment.point_of_intersection(segment_above, segment_below),
                                      [segment_above, segment_below]))
        else:
            segment1 = event_point.segment_identifier[0]#upper one
            segment2 = event_point.segment_identifier[1]#lower one
            point_of_intersection = Segment.point_of_intersection(segment1, segment2)
            set_of_intersection_points.add(point_of_intersection)
            tree.remove(segment1)
            tree.remove(segment2)

            segment1.currenty = point_of_intersection.y#lower
            segment2.currenty = point_of_intersection.y#upper
            tree.insert(segment1)
            tree.insert(segment2)

            segment_above = tree.get_succ(segment2)
            segment_below = tree.get_prev(segment1)

            if segment_above != None:
                segment_above = tree.get_succ(segment2).key
            if segment_below != None:
                segment_below = tree.get_prev(segment1).key

            if segment_above != None and Segment.do_intersect(segment2, segment_above):
                try:
                    if not visited[Segment.point_of_intersection(segment_above, segment2)]:
                        PQ.put(EventPoint("intersection", Segment.point_of_intersection(segment_above, segment2),
                                          [segment_above, segment2]))
                except KeyError:
                    PQ.put(EventPoint("intersection", Segment.point_of_intersection(segment_above, segment2),
                                      [segment_above, segment2]))

            if segment_below != None and Segment.do_intersect(segment1, segment_below):
                try:
                    if not visited[Segment.point_of_intersection(segment1, segment_below)]:
                        PQ.put(EventPoint("intersection", Segment.point_of_intersection(segment1, segment_below),
                                          [segment1, segment_below]))
                except KeyError:
                    PQ.put(EventPoint("intersection", Segment.point_of_intersection(segment1, segment_below),
                                      [segment1, segment_below]))
    return set_of_intersection_points


s1 = Segment(Point(0, 4), Point(4, 0))
s2 = Segment(Point(0, 2), Point(2, 0))
s3 = Segment(Point(0.5, 0.5), Point(3, 6))
lista = [s1, s2, s3]
print(get_intersections(lista))
print("----")

s1 = Segment(Point(-1, 1), Point(8, 10))
s2 = Segment(Point(1, 0), Point(4, 2))
s3 = Segment(Point(0, 3), Point(3, 0))
lista = [s1, s2, s3]
print(get_intersections(lista))
print("----")

s1 = Segment(Point(-3, 0), Point(0, -3))
s2 = Segment(Point(-5, -2), Point(0, -7))
s3 = Segment(Point(-4, -6), Point(0, 0))
lista = [s1, s2, s3]
print(get_intersections(lista))
print("----")
s1 = Segment(Point(1, 1), Point(2, 3))
s2 = Segment(Point(0, 4), Point(4, 0))
s3 = Segment(Point(0.5, 2), Point(4, 1))
s4 = Segment(Point(2, 2), Point(4, 3))
s5 = Segment(Point(5, 0.25), Point(5.01, 2))
s6 = Segment(Point(2.5, 1.5), Point(6, 1.51))
lista = [s1, s2, s3, s4, s5, s6]
print(get_intersections(lista))
print("----")
s1 = Segment(Point(1, 1), Point(5, 1))
s2 = Segment(Point(2, 5), Point(2, 0))
lista = [s1, s2]
print(get_intersections(lista))

print("hahu")