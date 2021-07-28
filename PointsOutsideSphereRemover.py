import math


def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


def main(x_pos, y_pos, z_pos, radius, points_array):
    array_copy = points_array
    points_outside = 0
    for point in points_array:
        if distance(x_pos, y_pos, z_pos, point[0], point[1], point[2]) > radius:
            points_outside += 1
            array_copy.remove(point)
    return points_outside, array_copy
