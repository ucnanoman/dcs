import math


def point_from_heading(_x, _y, heading, distance):
    heading %= 360
    rad_heading = math.radians(heading)
    x = _x + math.cos(rad_heading) * distance
    y = _y + math.sin(rad_heading) * distance

    return x, y


def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def heading_between_points(x1, y1, x2, y2):
    def angle_trunc(a):
        while a < 0.0:
            a += math.pi * 2
        return a
    deltax = x2 - x1
    deltay = y2 - y1
    return math.degrees(angle_trunc(math.atan2(deltay, deltax)))
