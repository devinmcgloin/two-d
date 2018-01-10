"""
Implements common distance functions
"""
from .primitives import Point
import math


def euclidean_distance(p1: Point, p2: Point) -> float:
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))


def manhattan_distance(p1: Point, p2: Point) -> float:
    return math.fabs(p1.x - p2.x) + math.fabs(p1.y - p2.y)
