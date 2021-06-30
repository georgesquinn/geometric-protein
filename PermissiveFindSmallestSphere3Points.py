import math
import CenterFrom3Points3DScript
import FindSmallestSphere2Points


def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


def main(points_array, allowance_constant):
    points_allowed_outside = len(points_array) * allowance_constant
    center_point = None
    radius = None
    privileged_sphere = False
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
                else:
                    points_outside = 0
                    # print(format(test_radius))
                    for Point in points_array:
                        if distance(Point[0], Point[1], Point[2], test_center[0], test_center[1],
                                    test_center[2]) > test_radius:
                            points_outside += 1
                        if points_outside > points_allowed_outside:
                            break
                    if points_outside > points_allowed_outside:
                        continue
                    else:
                        # print(format(test_radius))
                        if FindSmallestSphere2Points.main((point1, point2, point3)) is None:
                            privileged_sphere = True
                        else:
                            privileged_sphere = False
                        # print(format(test_radius))
                        radius = test_radius
                        center_point = test_center
    return radius, center_point, privileged_sphere
