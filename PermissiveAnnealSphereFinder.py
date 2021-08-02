import math
import random
import numpy as np
import decimal


def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By) + (Az - Bz) * (Az - Bz))


def generate_move(sphere_center, std_dev):
    theta = random.random() * math.pi
    phi = random.random() * 2 * math.pi
    point_radius = std_dev * .1 * random.random()
    x = point_radius * math.sin(theta) * math.cos(phi) + sphere_center[0]
    y = point_radius * math.sin(theta) * math.sin(phi) + sphere_center[1]
    z = point_radius * math.cos(theta) + sphere_center[2]
    return x, y, z


def anneal(sphere_center, points_array, std_dev, temperature, allowed_outside):
    current_radius = sphere_radius(sphere_center, points_array, allowed_outside)
    new_center = generate_move(sphere_center, std_dev)
    new_radius = sphere_radius(new_center, points_array, allowed_outside)
    if new_radius < current_radius:
        return new_center
    exponent = decimal.Decimal(-1 * ((new_radius - current_radius) / temperature))
    # e = decimal.Decimal(math.e)
    # probability = e ** exponent
    probability = exponent.exp()
    # exp raises e to the number it's used on
    if probability > random.random():
        return new_center
    return sphere_center


def main(points_array, exemption_constant):
    # Unset overflow trap since we're okay with rounding!
    # print(format(decimal.getcontext()))
    c = decimal.getcontext()
    c.traps[decimal.Overflow] = False
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
    std_dev = np.std(distance_array(center, points_array))
    radius = 0
    temperature = 1000
    while temperature > 0:
        temperature -= .1
        center = anneal(center, points_array, std_dev, temperature, allowed_outside)
    radius = sphere_radius(center, points_array, allowed_outside)
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
