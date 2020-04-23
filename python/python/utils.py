
import math
from typing import List


def heuristic(p: (int, int), q: (int, int)) -> float:
    """
    Helper function to compute distance between two points.
    :param p: (x,y)
    :param q: (x,y)
    :return: manhattan distance
    """
    return math.sqrt(abs(p[0] - q[0]) ** 2 + abs(p[1] - q[1]) ** 2)


def get_movements_4n(x: int, y: int) -> List:
    """
    get all possible 4-connectivity movements.
    :return: list of movements with cost [(dx, dy, movement_cost)]
    """
    return [(x + 1, y + 0),
            (x + 0, y + 1),
            (x - 1, y + 0),
            (x + 0, y - 1)]


def get_movements_8n(x: int, y: int) -> List:
    """
    get all possible 8-connectivity movements.
    :return: list of movements with cost [(dx, dy, movement_cost)]
    """
    return [(x + 1, y + 0),
            (x + 0, y + 1),
            (x - 1, y + 0),
            (x + 0, y - 1),
            (x + 1, y + 1),
            (x - 1, y + 1),
            (x - 1, y - 1),
            (x + 1, y - 1)]