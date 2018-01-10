'''
This file implements convex hull and associated helper functions
'''
from typing import List, Tuple, Callable
from .primitives import Point
from .common import argmin, cross
from .distance import euclidian_distance


def convex_hull(points: List[Point]) -> List[Point]:
    stack = []

    if len(points) <= 3:
        return points

    bottom, bottom_indx = bottommost(points)
    points.pop(bottom_indx)

    points.sort(key=polar_sort(bottom))
    points.insert(0, bottom)

    stack.append(points[0])
    stack.append(points[1])
    stack.append(points[2])

    for i in range(3, len(points)+1):
        stack.append(points[i % len(points)])
        while len(stack) > 2:
            m = len(stack)
            if left_turn(stack[m - 3], stack[m - 2], stack[m - 1]):
                break
            else:
                stack.pop(m - 2)
    stack.pop()
    return stack


def polar_sort(key_point: Point) -> Callable[[Point], Tuple[float, float]]:
    def rel(p: Point) -> Tuple[float, float]:
        polar = p.polar((key_point.x, key_point.y))
        return polar[1]

    return rel


def bottommost(points: List[Point]) -> Tuple[Point, int]:
    return argmin(points, lambda p: (p.y, p.x))


def left_turn(p1: Point, p2: Point, p3: Point) -> bool:
    return cross(p1, p2, p3) >= 0
