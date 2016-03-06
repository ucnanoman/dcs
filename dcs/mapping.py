import math
from typing import List, Tuple


def point_from_heading(_x, _y, heading, distance):
    """
    Calculates a point from a given point, heading and distance.
    :param _x: source point x
    :param _y: source point y
    :param heading: heading in degrees from source point
    :param distance: distance from source point
    :return: returns a tuple (x, y) of the calculated point
    """
    while heading < 0:
        heading += 360
    heading %= 360
    rad_heading = math.radians(heading)
    x = _x + math.cos(rad_heading) * distance
    y = _y + math.sin(rad_heading) * distance

    return x, y


def distance(x1, y1, x2, y2):
    """
    Returns the distance between 2 points
    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    :return: distance in point units(m)
    """
    return math.hypot(x2 - x1, y2 - y1)


def heading_between_points(x1, y1, x2, y2):
    """
    Returns the angle between 2 points in degrees.
    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    :return: angle in degrees
    """
    def angle_trunc(a):
        while a < 0.0:
            a += math.pi * 2
        return a
    deltax = x2 - x1
    deltay = y2 - y1
    return math.degrees(angle_trunc(math.atan2(deltay, deltax)))


class Rectangle:
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    @staticmethod
    def from_point(x, y, side_length):
        top = x + side_length / 2
        left = y - side_length / 2
        bottom = x - side_length / 2
        right = y + side_length / 2
        return Rectangle(top, left, bottom, right)

    def point_in_rect(self, x, y):
        return self.bottom <= x <= self.top and self.left <= y <= self.right


def point_in_poly(x, y, poly: List[Tuple[float, float]]):
    """
    Checks if the given point is within the polygon.
    :param x: x coordinate
    :param y: y coordinate
    :param poly: polygon points
    :return: True if point is within the polygon else False
    """
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside
