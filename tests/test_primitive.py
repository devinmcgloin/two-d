import twod.primitives as primitives
import math

def test_point_conversions():
    table = {
        # primitives.Point(0.0,2.0): (2, math.pi/2),
        # primitives.Point(0.0,1.0): (1, math.pi/2),
        primitives.Point(2.0,0.0): (1, 0.0),
        primitives.Point(1.0,1.0): (1, math.pi/2),
        primitives.Point(1.0,2.0): (2, math.pi / 2)
    }

    for p, expected in table.items():
        assert p.polar((1.0, 0.0)) == expected