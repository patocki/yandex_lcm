import math


def distance3d(set1, set2):
    return math.sqrt(
        (set1[0] - set2[0]) ** 2 + (set1[1] - set2[1]) ** 2 + (set1[2] - set2[2]) ** 2
    )
