import twod.distance as dist
import twod.primitives as p
from hypothesis import given
from hypothesis.strategies import tuples, floats


@given(
    p1=tuples(
        floats(max_value=9000, min_value=-9000, allow_nan=False),
        floats(max_value=9000, min_value=-9000, allow_nan=False)),
    p2=tuples(
        floats(max_value=9000, min_value=-9000, allow_nan=False),
        floats(max_value=9000, min_value=-9000, allow_nan=False)))
def test_euclidian_distance(p1, p2):
    pa = p.Point(p1[0], p1[0])
    pb = p.Point(p2[0], p2[1])
    d = dist.euclidian_distance(pa, pb)
    assert d >= 0


@given(
    p1=tuples(
        floats(max_value=9000, min_value=-9000, allow_nan=False),
        floats(max_value=9000, min_value=-9000, allow_nan=False)),
    p2=tuples(
        floats(max_value=9000, min_value=-9000, allow_nan=False),
        floats(max_value=9000, min_value=-9000, allow_nan=False)))
def test_manhattan_distance(p1, p2):
    pa = p.Point(p1[0], p1[0])
    pb = p.Point(p2[0], p2[1])
    d = dist.manhattan_distance(pa, pb)
    assert d >= 0
    assert d >= dist.euclidian_distance(pa, pb)
