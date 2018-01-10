"""
This file defines the basic primitives used by the rest of the package.
"""

EPS = 1e-9


class Point:
    def __init__(self, x, y):
        if not isinstance(x, float) or not isinstance(y, float):
            raise ValueError("either x or y are not floats")
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)


class LineSegment:
    def __init__(self, a, b):
        if not isinstance(a, Point) or not isinstance(b, Point):
            raise ValueError("either a or b are not points")
        self.a = a
        self.b = b


class Angle:
    def __init__(self, a, b, c):
        if not isinstance(a, Point) or not isinstance(
                b, Point) or not isinstance(b, Point):
            raise ValueError("either a, b or c are not points")
        self.a = a
        self.b = b
        self.c = c


class Polygon:
    def __init__(self, points):
        for p in points:
            if not isinstance(p, Point):
                raise ValueError("one item in array is not of type point")
        self.points = points
