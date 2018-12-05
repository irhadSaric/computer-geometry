from math import sqrt
from math import acos

def find_most_left(vertices):
    return min(vertices, key = lambda v: (v[0], -v[1]))

def dot(vector1, vector2):
    return vector1[0]*vector2[0] + vector1[1]*vector2[1]

def magnitude(vector):
    return sqrt(dot(vector, vector))

def euclidean_distance(vector):
    return sqrt(vector[0]**2 + vector[1]**2)

def angle(imaginaryPoint, mostLeft, v):
    mostLeftVector = (imaginaryPoint[0]-mostLeft[0], imaginaryPoint[1]-mostLeft[1])
    currentVector = (v[0]-mostLeft[0], v[1]-mostLeft[1])
    angle = acos((dot(mostLeftVector, currentVector))/magnitude(mostLeftVector)/magnitude(currentVector))
    return (angle, euclidean_distance(currentVector))

def simplePoly(vertices):
    mostLeft = find_most_left(vertices)
    imaginaryPoint = (mostLeft[0]-1, mostLeft[1])
    mostLeftIndex = vertices.index(mostLeft)
    vertices[0], vertices[mostLeftIndex] = vertices[mostLeftIndex], vertices[0]

    return vertices[0] + sorted(vertices[1:], key = lambda v : angle(imaginaryPoint, mostLeft, v))
