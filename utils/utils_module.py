# utils/utils_module.py
import math
import random

def calculate_distance(coord1, coord2):
    """
    Oblicza odległość euklidesową między dwoma punktami.
    coord1 i coord2 to krotki (x, y, z).
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(coord1, coord2)))

def random_position_on_boundary(airspace_dimensions):
    """
    Generuje losową pozycję na granicy przestrzeni.
    airspace_dimensions to krotka (width, height, depth).
    Losujemy stronę granicy dla osi x lub y, a z ustawiamy losowo w przedziale [2000, 5000].
    """
    width, height, depth = airspace_dimensions
    side = random.choice(['x0', 'xw', 'y0', 'yh'])
    if side == 'x0':
        x = 0
        y = random.uniform(0, height)
    elif side == 'xw':
        x = width
        y = random.uniform(0, height)
    elif side == 'y0':
        y = 0
        x = random.uniform(0, width)
    else:  # 'yh'
        y = height
        x = random.uniform(0, width)
    z = random.uniform(2000, 5000)
    return (x, y, z)
