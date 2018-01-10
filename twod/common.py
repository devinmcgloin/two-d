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
