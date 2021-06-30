# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:04:49 2021

@author: Peter
"""

import math
import numpy as np
import FindSmallestSphere3Points
import random
import FindSmallestSphere2Points
def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By) + (Az-Bz)*(Az-Bz))


x_center = math.tan(math.pi/4 * (random.random() + 1))
y_center = math.tan(math.pi/4 * (random.random() + 1))
z_center = math.tan(math.pi/4 * (random.random() + 1))
radius = math.tan(math.pi/4 * (random.random() + 1))
extra_radius = math.tan(math.pi/2 * random.random())
points_array = []
for i in range(100):
    theta = random.random() * math.pi
    phi = random.random() * 2*math.pi
    point_radius = (radius + extra_radius) * random.random()
    x = point_radius * math.sin(theta) * math.cos(phi) + x_center
    y = point_radius * math.sin(theta) * math.sin(phi) + y_center
    z = point_radius * math.cos(theta) + z_center
    points_array.append((x, y, z))
for i in range(0):
    theta = random.random() * math.pi
    phi = random.random() * 2 * math.pi
    x = (radius + extra_radius * .999) * math.sin(theta) * math.cos(phi) + x_center
    y = (radius + extra_radius * .999) * math.sin(theta) * math.sin(phi) + y_center
    z = (radius + extra_radius * .999) * math.cos(theta) + z_center
    points_array.append((x, y, z))
    #print(format((x, y, z)))
#print(format(points_array))
alpha = random.random() * 2 * math.pi
beta = random.random() * 2 * math.pi
gamma = random.random() * 2 * math.pi
a_angle = random.random() * 2 * math.pi
b_angle = random.random() * 2 * math.pi
c_angle = random.random() * 2 * math.pi
point_a = np.vstack([(radius + extra_radius) * math.cos(a_angle), (radius + extra_radius) * math.sin(a_angle), 0])
point_b = np.vstack([(radius + extra_radius) * math.cos(b_angle), (radius + extra_radius) * math.sin(b_angle), 0])
point_c = np.vstack([(radius + extra_radius) * math.cos(c_angle), (radius + extra_radius) * math.sin(c_angle), 0])
rot_matrix_yaw = [[math.cos(alpha), -1 * math.sin(alpha), 0],
                  [math.sin(alpha), math.cos(alpha), 0],
                  [0, 0, 1]]
rot_matrix_pitch = [[math.cos(beta), 0, math.sin(beta)],
                    [0, 1, 0],
                    [-1 * math.sin(beta), 0, math.cos(beta)]]
rot_matrix_roll = [[1, 0, 0],
                   [0, math.cos(gamma), -1 * math.sin(gamma)],
                   [0, math.sin(gamma), math.cos(gamma)]]
RotMatrix = np.matmul(np.matmul(rot_matrix_yaw, rot_matrix_pitch), rot_matrix_roll)
# RotMatrix = [[math.cos(alpha)*math.cos(beta), (math.cos(alpha)*math.sin(beta)*math.sin(gamma)) - (math.sin(alpha)*math.cos(gamma)), (math.cos(alpha)*math.sin(beta)*math.cos(gamma)) + (math.sin(alpha)*math.sin(gamma))],
#               [math.sin(alpha)*math.cos(beta), (math.sin(alpha)*math.sin(beta)*math.sin(gamma)) - (math.cos(alpha)*math.cos(gamma)), (math.sin(alpha)*math.sin(beta)*math.cos(gamma)) - (math.cos(alpha)*math.sin(gamma))],
#               [-math.sin(beta), math.cos(beta)*math.sin(gamma), math.cos(beta)*math.cos(gamma)]]
# rot_matrix_transpose = np.transpose(RotMatrix)
# print("Determinant: " + format(np.linalg.det(RotMatrix)))
# print("Mult'd by transpose: " + format(np.matmul(RotMatrix, rot_matrix_transpose)))
a_prime = np.matmul(RotMatrix, point_a)
b_prime = np.matmul(RotMatrix, point_b)
c_prime = np.matmul(RotMatrix, point_c)
#print(format(a_prime))
points_array.append((a_prime[0][0] + x_center, a_prime[1][0] + y_center, a_prime[2][0] + z_center))
points_array.append((b_prime[0][0] + x_center, b_prime[1][0] + y_center, b_prime[2][0] + z_center))
points_array.append((c_prime[0][0] + x_center, c_prime[1][0] + y_center, c_prime[2][0] + z_center))
#print(format(points_array))
print(format(FindSmallestSphere2Points.main(((a_prime[0][0] + x_center, a_prime[1][0] + y_center, a_prime[2][0] + z_center), (b_prime[0][0] + x_center, b_prime[1][0] + y_center, b_prime[2][0] + z_center),(c_prime[0][0] + x_center, c_prime[1][0] + y_center, c_prime[2][0] + z_center) ))))
print("Inner radius is: " + format(radius))
print("Total radius is: " + format(radius + extra_radius))
print("Actual center is at (" + format(x_center) + ", " + format(y_center) + ", " + format(z_center) + ")")
#print("Distance between 2 extremes is: " + format(distance(x_one, y_one, z_one, x_two, y_two, z_two)))
sphere_produced = FindSmallestSphere3Points.main(points_array)
print("Calculated radius is: " + format(sphere_produced[0]))
print("Calculated center is: " + format(sphere_produced[1]))