from vector import *
from bintrees import AVLTree
from heapq import *

def getIntersections(segments: list) -> list:
    tree = AVLTree()
    priorityQueue = []
    listOfIntersections = set()

    i = 0
    for segment in segments:

        heappush(priorityQueue, EventPoint("s", i, segment.head))
        heappush(priorityQueue, EventPoint("e", i, segment.tail))
        i += 1

    while priorityQueue.__len__() != 0:
        event = heappop(priorityQueue)  # Tacka na koju se nailazi

        if event.eventType == "s":
            segment = segments[event.index]  # Segment koji sadrzi tacku
            tree.insert(event.index, (segment, event.index))

            try:
                segmentAbove = tree.prev_item(event.index)[1][0]
                segmentAboveID = tree.prev_item(event.index)[1][1]
            except KeyError:
                segmentAbove = None

            try:
                segmentBelow = tree.succ_item(event.index)[1][0]
                segmentBelowID = tree.prev_item(event.index)[1][1]
            except KeyError:
                segmentBelow = None

            if segmentAbove != None and segmentBelow != None:
                if Vector.do_intersect(segmentAbove, segmentBelow):
                    """print(tree.get_value(event.index)[0].head)
                    print(segmentAbove.head)
                    print(segmentBelow.head)
                    print(Vector.point_of_intersection(segmentAbove, flightBelow))"""
                    if Vector.point_of_intersection(segmentAbove, segmentBelow) in priorityQueue:
                        priorityQueue.remove(Vector.point_of_intersection(segmentAbove, segmentBelow))

            if segmentAbove != None:
                if Vector.do_intersect(segmentAbove, segment):
                    heappush(priorityQueue, EventPoint("i", (segmentAboveID, event.index), Vector.point_of_intersection(segmentAbove, segment)))
            if segmentBelow != None:
                if Vector.do_intersect(segmentBelow, segment):
                    heappush(priorityQueue, EventPoint("i", (event.index, segmentBelowID), Vector.point_of_intersection(segmentBelow, segment)))

        elif event.eventType == "e":
            segment = segments[event.index]
            try:
                segmentAbove = tree.prev_item(event.index)[1][0]
                segmentAboveID = tree.prev_item(event.index)[1][1]
            except KeyError:
                segmentAbove = None

            try:
                segmentBelow = tree.succ_item(event.index)[1][0]
                segmentBelowID = tree.succ_item(event.index)[1][1]
            except KeyError:
                segmentBelow = None

            tree.remove(event.index)
            if segmentAbove != None and segmentBelow != None:
                if Vector.do_intersect(segmentAbove, segmentBelow):
                    heappush(priorityQueue, EventPoint("i", (segmentAboveID, segmentBelowID), Vector.point_of_intersection(segmentAbove, segmentBelow)))
        else:
            listOfIntersections.add((event.x, event.y))
            print(listOfIntersections)

    print("____")

s1 = Vector(Point(0.0, 4.0), Point(5.0, 0.0))
s2 = Vector(Point(0.5, 2.0), Point(4.0, 1.0))
s3 = Vector(Point(2.0, 2.0), Point(4.0, 3.0))
s4 = Vector(Point(1.0, 1.0), Point(2.0, 3.0))
s5 = Vector(Point(5.0, 0.0), Point(5.0, 3.0))
s6 = Vector(Point(1.375, 1.75), Point(5.0, 1.75))
lista = [s1, s2, s3, s4, s5, s6]

getIntersections(lista)

"""
Algoritam: https://www.hackerearth.com/practice/math/geometry/line-intersection-using-bentley-ottmann-algorithm/tutorial/

Pitati:
    1. Izbacivanje linija 42-43, kako napraviti u log vremenu
    2. Zbog cega se treba izvrsiti zamjena u stablu u else bloku, kad radi i ovako, tj. da li postoji neki slucaj kada
       trenutni program ne bi radio ili bi mu se pokvarila kompleksnost ?
    3. Ako se treba zavrsiti izmjena, kako
    4. Da li se na isti fol moze uraditi i projekat, samo sto bi se razlikovala fja point_of_intersection
"""