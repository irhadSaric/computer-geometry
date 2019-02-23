from Point import *

def find_most_left_vertex(vertices):
    return min(vertices, key = lambda x: (x[0], -x[1]))

def divide_vertices(vertices, mostLeftVertex):
    upperHull = []
    lowerHull = []
    for v in vertices:
        if v[1] > mostLeftVertex[1]:
            upperHull.append(v)
        else:
            lowerHull.insert(0, v)
    return upperHull, lowerHull

def find_hull(vertices):
    hull = []
    hull.append(vertices[0])
    hull.append(vertices[1])

    for v in vertices[2:]:
        while Point.orientation(Point(*hull[-2]), Point(*hull[-1]), Point(*v)) > 0:
            hull.pop()
        hull.append(v)

    return hull

def GrahamScan(vertices):
    mostLeftVertex = find_most_left_vertex(vertices)
    vertices.sort()
    upperVertices, lowerVertices = divide_vertices(vertices, mostLeftVertex)
    upperHull = find_hull(upperVertices)
    lowerHull = find_hull(lowerVertices)
    return upperHull+lowerHull