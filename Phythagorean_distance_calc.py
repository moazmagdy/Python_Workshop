"""
In this document we will use Phythagorean method
to calculate the distance between three points
Steps:
1. values of the three points 2, 3, and 4
    are assigned to
x, y, and z variables.
2. we will sum the squares of these points.
3. We take the square roots.
"""
import math
x, y, z = 2, 3, 4
pyth_distance = math.sqrt(x**2 + y**2 + z**2)
print(pyth_distance)