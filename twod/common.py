from typing import List
import math

from .primitives import Point, EPS
from .distance import euclidian_distance


def area(points: List[Point]) -> float:
    """
    This function should first break the polygon up into triangles and sum
    them. This avoids clockwise / counterclockwise algorithms that are simplier
    to implement but more fragile.

    It will still not handle polygons that fold onto themselves.
    """
    pass


def perimeter(points: List[Point], dist=euclidian_distance) -> float:
    """
    perimeter calculates the perimeter of the polygon with the given distance
    metric. By default euclidian distance.
    """
    acc = 0.0
    for i, _ in enumerate(points):
        n = (i + 1) % len(points)
        acc += dist(points[i], points[n])
    return acc


def inside(poly: List[Point], p: Point) -> bool:
    '''
    Determines if point is inside polygon using the winding number method
    '''
    wn = 0
    for i in range(len(poly)):
        n = (i + 1) % len(poly)
        if poly[i].y <= p.y and poly[n].y > p.y and cross(poly[i], poly[n],
                                                          p) > 0:
            wn += 1
        elif poly[n].y <= p.y and cross(poly[i], poly[n], p) < 0:
            wn -= 1
    return wn != 0


def cross(p1: Point, p2: Point, p3: Point) -> float:
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def argmin(l, f=lambda x: x):
    if len(l) == 0:
        return None, None
    item = l[0]
    min_val = f(item)
    indx = 0
    for i, v in enumerate(l):
        if f(v) <= min_val:
            min_val = f(v)
            item = v
            indx = i
    return item, indx


def argmax(l, f=lambda x: x):
    return argmin(l, lambda x: -f(x))
