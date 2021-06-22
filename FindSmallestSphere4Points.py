import sys
import numpy as np
import math
import CenterFrom4Points3DScript


def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


def main(points_array):
    center_point = None
    radius = None
    for point1 in points_array:
        for point2 in points_array:
            if point2 == point1:
                continue
            for point3 in points_array:
                if point3 == point1 or point3 == point2:
                    continue
                for point4 in points_array:
                    if point4 == point1 or point4 == point2 or point4 == point3:
                        continue
                    test_center = CenterFrom4Points3DScript.main(point1[0], point1[1], point1[2], point2[0], point2[1],
                                                                 point2[2], point3[0], point3[1], point3[2], point4[0],
                                                                 point4[1], point4[2])
                    test_radius = distance(point1[0], point1[1], point1[2], test_center[0], test_center[1],
                                           test_center[2])
                    # print(format(test_radius))
                    if radius is not None and test_radius > radius:
                        continue
                    else:
                        encloses = True
                        for Point in points_array:
                            if distance(Point[0], Point[1], Point[2], test_center[0], test_center[1],
                                        test_center[2]) > test_radius:
                                encloses = False
                                break
                        if not encloses:
                            continue
                        else:
                            # print(format(radius))
                            # print(format(point1) + format(point2) + format(point3) + format(point4))
                            radius = test_radius
                            center_point = test_center
    return (radius, center_point)
