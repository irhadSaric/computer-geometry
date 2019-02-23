from Point import *

def find_centroid(edges):
    xCoordinate = 0.0
    yCoordinate = 0.0
    for edge in edges:
        xCoordinate += edge[0][0] + edge[1][0]
        yCoordinate += edge[0][1] + edge[1][1]
    return (xCoordinate / len(edges), yCoordinate / len(edges))

def orientate_edges(edges, centroid):
    for i, edge in enumerate(edges):
        if Point.orientation(Point(*edge[0]), Point(*edge[1]), Point(*centroid)) == 0:
            lista = list(edges[i])
            lista.reverse()
            edges[i] = tuple(lista)

def construct_vertices_map(edges):
    map = dict()
    for edge in edges:
        map[edge[0]] = edge[1]
    map[0] = edges[0][0]
    return map

def traverse_map(verticesMap):
    sortedVertices = []
    sortedVertices.append(verticesMap[0])
    vertex = verticesMap[sortedVertices[0]]
    while vertex != sortedVertices[0]:
        sortedVertices.append(vertex)
        vertex = verticesMap[vertex]
    return sortedVertices

def sort_cw(edges):
    centroid = find_centroid(edges)
    orientate_edges(edges, centroid)
    verticesMap = construct_vertices_map(edges)
    return traverse_map(verticesMap)