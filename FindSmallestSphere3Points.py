import sys
import numpy as np
import math
import CenterFrom3Points3DScript
import FindSmallestSphere2Points


def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


# Note: Does not find non-privilged 3-point circles!!!! Saves time, but need to edit logic for that to
# happen again. Look at previous github versions before 6/28/21 for the file that finds non-privileged
# 3-point spheres!
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
                test_center = CenterFrom3Points3DScript.main(point1[0], point1[1], point1[2], point2[0], point2[1],
                                                             point2[2], point3[0], point3[1], point3[2])
                test_radius = distance(point1[0], point1[1], point1[2], test_center[0], test_center[1], test_center[2])
                if radius is not None and test_radius > radius:
                    continue
                if FindSmallestSphere2Points.main((point1, point2, point3)) is not None:
                    continue
                else:
                    encloses = True
                    # print(format(test_radius))
                    for Point in points_array:
                        if distance(Point[0], Point[1], Point[2], test_center[0], test_center[1],
                                    test_center[2]) > test_radius:
                            encloses = False
                            break
                    if not encloses:
                        continue
                    else:
                        return test_radius, test_center, True
    return radius, center_point, False
