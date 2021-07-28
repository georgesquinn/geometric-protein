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
    allowed_outside = round(len(points_array) * exemption_constant)
    center = (x_avg, y_avg, z_avg)
    radius = sphere_radius(center, points_array, allowed_outside)
    iterating = True
    jiggle_constant = .5
    while iterating:
        iterating = False
        left_jiggle = (center[0] - jiggle_constant, center[1], center[2])
        right_jiggle = (center[0] + jiggle_constant, center[1], center[2])
        down_jiggle = (center[0], center[1] - jiggle_constant, center[2])
        up_jiggle = (center[0], center[1] + jiggle_constant, center[2])
        back_jiggle = (center[0], center[1], center[2] - jiggle_constant)
        front_jiggle = (center[0], center[1], center[2] + jiggle_constant)
        left_jiggle_radius = sphere_radius(left_jiggle, points_array, allowed_outside)
        if left_jiggle_radius < radius:
            iterating = True
            jiggle_constant = .5
            center = left_jiggle
            radius = left_jiggle_radius
            continue
        right_jiggle_radius = sphere_radius(right_jiggle, points_array, allowed_outside)
        if right_jiggle_radius < radius:
            iterating = True
            jiggle_constant = .5
            center = right_jiggle
            radius = right_jiggle_radius
            continue
        down_jiggle_radius = sphere_radius(down_jiggle, points_array, allowed_outside)
        if down_jiggle_radius < radius:
            iterating = True
            jiggle_constant = .5
            center = down_jiggle
            radius = down_jiggle_radius
            continue
        up_jiggle_radius = sphere_radius(up_jiggle, points_array, allowed_outside)
        if up_jiggle_radius < radius:
            iterating = True
            jiggle_constant = .5
            center = up_jiggle
            radius = up_jiggle_radius
            continue
        back_jiggle_radius = sphere_radius(back_jiggle, points_array, allowed_outside)
        if back_jiggle_radius < radius:
            iterating = True
            jiggle_constant = .5
            center = back_jiggle
            radius = back_jiggle_radius
            continue
        front_jiggle_radius = sphere_radius(front_jiggle, points_array, allowed_outside)
        if front_jiggle_radius < radius:
            iterating = True
            jiggle_constant = .5
            center = front_jiggle
            radius = front_jiggle_radius
            continue
        if jiggle_constant < 100:
            iterating = True
            if jiggle_constant < 10:
                jiggle_constant += .5
            elif jiggle_constant < 20:
                jiggle_constant += 1
            else:
                jiggle_constant += 10
    return radius, center


def distance_array(center_point, points_array):
    distances = []
    for point in points_array:
        distances.append(distance(center_point[0], center_point[1], center_point[2], point[0], point[1], point[2]))
    distances.sort(reverse=True)
    # Setting reverse to True gets us descending order, which is what we want!
    return distances


def sphere_radius(center_point, points_array, allowed_outside):
    dist_array = distance_array(center_point, points_array)
    # Off by one is handled here, since you go one element deeper in than the number allowed outside.
    return dist_array[allowed_outside]
