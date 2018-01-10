from typing import List

from .primitives import Point
from .distance import euclidean_distance


def area(points: List[Point]) -> float:
    """
    This function should first break the polygon up into triangles and sum
    them. This avoids clockwise / counterclockwise algorithms that are simpler
    to implement but more fragile.

    It will still not handle polygons that fold onto themselves.
    """
    pass


def perimeter(poly: List[Point], dist=euclidean_distance) -> float:
    """
    perimeter calculates the perimeter of the polygon.
    :param poly: list of points in which the first element is not the last.
    :param dist: distance function to be used, by default euclidean distance.
    :return: the perimeter of the polygon.
    """
    acc = 0.0
    for i, _ in enumerate(poly):
        n = (i + 1) % len(poly)
        acc += dist(poly[i], poly[n])
    return acc


def inside(poly: List[Point], p: Point) -> bool:
    """
    Determines if point is inside polygon using the winding number method
    :param poly: polygon to be checked. poly[0] != poly[len(poly)].
    That is the shape should not be closed. The function takes care of closing the shape itself.
    :param p: point to be checked
    :return: true iff p is inside poly. If p is on one of the edges of the polygon the
    inside will return false.
    """
    poly.append(poly[0])
    wn = 0
    for i in range(len(poly)):
        n = (i + 1) % len(poly)
        if poly[i].y <= p.y < poly[n].y and cross(poly[i], poly[n],
                                                  p) > 0:
            wn += 1
        elif poly[n].y <= p.y and cross(poly[i], poly[n], p) < 0:
            wn -= 1
    return wn != 0


def cross(p1: Point, p2: Point, p3: Point) -> float:
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def arg_min(l, f=lambda x: x):
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


def arg_max(l, f=lambda x: x):
    return arg_min(l, lambda x: -f(x))
