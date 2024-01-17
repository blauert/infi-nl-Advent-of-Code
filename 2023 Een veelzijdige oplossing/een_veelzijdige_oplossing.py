# https://aoc.infi.nl/2023/

import math
import re
from shapely import Polygon, minimum_bounding_radius

input_file = "real_input.txt"
#input_file = 'test_input.txt'

coordinates = re.compile(r"\((-?\d+), (-?\d+)\)")

with open(input_file) as file:
    pakjes = [
        [(int(x), int(y)) for x, y in coordinates.findall(line)]
        for line in file.readlines()
    ]


# Deel 1

radii = 0

for pakje in pakjes:
    max_radius = 0
    for x, y in pakje:
        dist = math.sqrt(x**2 + y**2)
        max_radius = max(max_radius, dist)
    radii += max_radius

print(f"Deel 1: {int(radii)}")


# Deel 2

radii = 0

for pakje in pakjes:
    radii += minimum_bounding_radius(Polygon(pakje))

print(f"Deel 2: {int(radii)}")
