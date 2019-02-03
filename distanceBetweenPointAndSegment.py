from math import sqrt

def distancePtoS(point, segment):
    x = point[0]
    y = point[1]
    x1 = segment[0][0]
    y1 = segment[0][1]
    x2 = segment[1][0]
    y2 = segment[1][1]

    A = x - x1
    B = y - y1
    C = x2 - x1
    D = y2 - y1

    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1

    if (len_sq != 0): #// in case of 0 length line
        param = dot / len_sq

    if (param < 0):
        xx = x1
        yy = y1

    elif param > 1:
        xx = x2
        yy = y2

    else:
        xx = x1 + param * C
        yy = y1 + param * D

    dx = x - xx
    dy = y - yy

    return sqrt(dx * dx + dy * dy)