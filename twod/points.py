from .primitives import Point
from typing import Tuple, List
from .distance import euclidean_distance

def closest_pair(points: List[Point], dist=euclidean_distance) -> Tuple[Point, Point]:
    '''
    This would be simpler to implement with Delaunay Triangulation on hand.
    :param points:
    :param dist:
    :return:
    '''
    pass

