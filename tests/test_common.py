from twod.primitives import Point, EPS
from twod.common import area, perimeter, argmax, argmin, inside
from hypothesis import given
from hypothesis.strategies import tuples, floats, lists, integers
import math

# @given(
# points=lists(
# tuples(
# floats(
# max_value=9000,
# min_value=0,
# allow_infinity=False,
# allow_nan=False),
# floats(
# max_value=9000,
# min_value=0,
# allow_infinity=False,
# allow_nan=False))))
# def test_area_generative(points):
# ps = [Point(p[0], p[1]) for p in points]
# a = area(ps)
# assert a >= 0

# def test_area():
# points = [(4.0, 6.0), (4.0, -4.0), (8.0, -4.), (8.0, -8.0), (-4.0, -8.0),
# (-4.0, 6.0)]
# ps = [Point(p[0], p[1]) for p in points]
# a = area(ps)
# assert a >= 0


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

@given(xs=lists(integers(), min_size=1))
def test_argmin(xs):
    x, indx = argmin(xs)
    m = min(xs)
    last_index = -1
    for i, v in enumerate(xs):
        if m == v:
            last_index = i
    assert x == m
    assert indx == last_index

@given(xs=lists(integers(),min_size=1))
def test_argmax(xs):
    x, indx = argmax(xs)
    m = max(xs)
    last_index = -1
    for i, v in enumerate(xs):
        if m == v:
            last_index = i
    assert x == m
    assert indx == last_index


def test_inside():
    points = [Point(0.0, 0.0), Point(4.0, 0.0), Point(0.0, 3.0), Point(0.0, 2.0), Point(0.0, 0.0)]
    p = Point(1.0, 2.0)
    assert inside(points, p)

