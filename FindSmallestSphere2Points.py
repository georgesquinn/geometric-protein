# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:13:01 2021

@author: George Quinn
"""
import math


def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


def main(points_array):
    for point1 in points_array:
        for point2 in points_array:
            if point2 == point1:
                continue
            test_center = (((point1[0] + point2[0]) / 2), ((point1[1] + point2[1]) / 2), ((point1[2] + point2[2]) / 2))
            test_radius = distance(test_center[0], test_center[1], test_center[2], point1[0], point1[1], point1[2])
            encloses = True
            for Point in points_array:
                # print(format(test_radius))
                if distance(Point[0], Point[1], Point[2], test_center[0], test_center[1], test_center[2]) > test_radius:
                    encloses = False
                    break
            if encloses == False:
                continue
            else:
                return (test_radius, test_center)
    return None
