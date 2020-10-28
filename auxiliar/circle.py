# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:50:32 2018

@author: Rodrigo
"""

from math import sqrt
import random


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class Circle:
    def __init__(self, a, b, c):
        s1 = Point((a.x + b.x) / 2.0, (a.y + b.y) / 2.0)
        d1 = Point(b.y - a.y, a.x - b.x)
        s2 = Point((a.x + c.x) / 2.0, (a.y + c.y) / 2.0)
        d2 = Point(c.y - a.y, a.x - c.x)
        l = d1.x * (s2.y - s1.y) - d1.y * (s2.x - s1.x)
        l = l / (d2.x * d1.y - d2.y * d1.x)
        self.center = Point(s2.x + l * d2.x, s2.y + l * d2.y)
        dx = self.center.x - a.x
        dy = self.center.y - a.y
        self.radius = sqrt(dx * dx + dy * dy)


def isCircular(self, radioReal, factor):
    radioReal = float(radioReal)
    if abs(1.0 - (self.radius / radioReal)) < factor:
        return True
    else:
        return False


def createCircle(a, b, c):
    x = Point(a[0], a[1])
    y = Point(b[0], b[1])
    z = Point(c[0], c[1])

    return Circle(x, y, z)


def pick3RandomPoints(points):
    return random.sample(points, 3)
