# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:13:01 2021

@author: George Quinn
"""
import math


def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


def main(points_array, allowance_constant):
    points_allowed_outside = len(points_array) * allowance_constant
    center_point = None
    radius = None
    for point1 in points_array:
        for point2 in points_array:
            if point2 == point1:
                continue
            test_center = (((point1[0] + point2[0]) / 2), ((point1[1] + point2[1]) / 2), ((point1[2] + point2[2]) / 2))
            test_radius = distance(test_center[0], test_center[1], test_center[2], point1[0], point1[1], point1[2])
            points_outside = 0
            if radius is not None and \
                    distance(point1[0], point1[1], point1[2], test_center[0], test_center[1], test_center[2]) > radius:
                continue
            for point in points_array:
                if distance(point[0], point[1], point[2], test_center[0], test_center[1], test_center[2]) > test_radius:
                    points_outside += 1
                if points_outside > points_allowed_outside:
                    break
            if points_outside > points_allowed_outside:
                continue
            else:
                # print(format(test_radius))
                radius = test_radius
                center_point = test_center
    return (radius, center_point)
