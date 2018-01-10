from twod.primitives import Point, EPS
from twod.common import area, perimeter
from hypothesis import given
from hypothesis.strategies import tuples, floats, lists
import math


@given(
    points=lists(
        tuples(
            floats(
                max_value=9000,
                min_value=0,
                allow_infinity=False,
                allow_nan=False),
            floats(
                max_value=9000,
                min_value=0,
                allow_infinity=False,
                allow_nan=False))))
def test_area_generative(points):
    ps = [Point(p[0], p[1]) for p in points]
    a = area(ps)
    assert a >= 0


def test_area():
    points = [(4.0, 6.0), (4.0, -4.0), (8.0, -4.), (8.0, -8.0), (-4.0, -8.0),
              (-4.0, 6.0)]
    ps = [Point(p[0], p[1]) for p in points]
    a = area(ps)
    assert a >= 0


@given(
    points=lists(
        tuples(
            floats(
                max_value=9000,
                min_value=0,
                allow_infinity=False,
                allow_nan=False),
            floats(
                max_value=9000,
                min_value=0,
                allow_infinity=False,
                allow_nan=False))))
def test_perimeter_generative(points):
    ps = [Point(p[0], p[1]) for p in points]
    a = perimeter(ps)
    assert a >= 0


def test_perimeter():
    points = [(0.0, 0.0), (0.0, 1000.0), (1000.0, 0.0)]
    ps = [Point(p[0], p[1]) for p in points]
    a = perimeter(ps)
    assert a >= 0
    assert math.fabs(a - 3414.21356237309504880168872420969807856967) < EPS
