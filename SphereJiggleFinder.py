import PointsOutsideSphereRemover
import math

def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


def main(points_array, exemption_constant):
    x_avg = 0
    y_avg = 0
    z_avg = 0
    for point in points_array:
        x_avg += point[0]
        y_avg += point[1]
        z_avg += point[2]
    x_avg /= len(points_array)
    y_avg /= len(points_array)
    z_avg /= len(points_array)
    center = (x_avg, y_avg, z_avg)
    iterating = False
