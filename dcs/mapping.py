import math
import random
import copy
from typing import List


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


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point_from_heading(self, heading, distance):
        x, y = point_from_heading(self.x, self.y, heading, distance)
        return Point(x, y)

    def heading_between_point(self, point):
        return heading_between_points(self.x, self.y, point.x, point.y)

    def distance_to_point(self, point):
        return distance(self.x, self.y, point.x, point.y)

    def __repr__(self):
        return "Point({x}, {y})".format(x=self.x, y=self.y)


class Rectangle:
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    @staticmethod
    def from_point(point: Point, side_length):
        top = point.x + side_length / 2
        left = point.y - side_length / 2
        bottom = point.x - side_length / 2
        right = point.y + side_length / 2
        return Rectangle(top, left, bottom, right)

    def point_in_rect(self, point: Point):
        return self.bottom <= point.x <= self.top and self.left <= point.y <= self.right

    def height(self):
        return self.top - self.bottom

    def width(self):
        return self.right - self.left

    def center(self) -> Point:
        return Point(self.bottom + (self.height() / 2), self.left + (self.width() / 2))

    def random_int_point(self) -> Point:
        x = random.randrange(int(self.bottom), int(self.top))
        y = random.randrange(int(self.left), int(self.right))
        return Point(x, y)

    def __repr__(self):
        return "Rectangle({t}, {l}, {b}, {r})".format(t=self.top, l=self.left, b=self.bottom, r=self.right)


class Polygon:
    def __init__(self, points: List[Point]=None):
        if points is None:
            points = []
        self.points = copy.copy(points)

    def point_in_poly(self, point: Point):
        """
        Checks if the given point is within the polygon.
        :param point: Point to test
        :return: True if point is within the polygon else False
        """
        n = len(self.points)
        inside = False

        p1x = self.points[0].x
        p1y = self.points[0].y
        for i in range(n+1):
            p = self.points[i % n]
            p2x = p.x
            p2y = p.y
            if point.y > min(p1y, p2y):
                if point.y <= max(p1y, p2y):
                    if point.x <= max(p1x, p2x):
                        if p1y != p2y:
                            xints = (point.y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or point.x <= xints:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

    def random_point(self) -> Point:
        # stupid and slow
        minx = min([p.x for p in self.points])
        maxx = max([p.x for p in self.points])
        miny = min([p.y for p in self.points])
        maxy = max([p.y for p in self.points])

        r = Rectangle(maxx, miny, minx, maxy)
        while True:
            p = r.random_int_point()
            if self.point_in_poly(p):
                break

        return p
