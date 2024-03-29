import math

type Number = int | float
type Coordinate2D = tuple[Number, Number]
type Coordinate3D = tuple[Number, Number, Number]


def squared(n):
    return pow(n, 2)


def distance_2d(a: Coordinate2D, b: Coordinate2D):
    return math.sqrt(squared(a[0] - b[0] + squared(a[1] - b[1])))


def distance_3d(a: Coordinate3D, b: Coordinate3D):
    return math.sqrt(squared(a[0] - b[0]) + squared(a[1] - b[1]) + squared(a[2] - b[2]))


def windowed(items: list, window_size: int):
    for i in range(len(items) - window_size + 1):
        yield items[i : i + window_size]
