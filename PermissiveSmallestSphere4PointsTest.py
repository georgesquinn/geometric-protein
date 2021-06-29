# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:39:04 2021

@author: Peter
"""

import math
import numpy as np
import PermissiveFindSmallestSphere4Points
import random

def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By) + (Az-Bz)*(Az-Bz))


x_center = math.tan(math.pi/4 * (random.random() + 1))
y_center = math.tan(math.pi/4 * (random.random() + 1))
z_center = math.tan(math.pi/4 * (random.random() + 1))
radius = math.tan(math.pi/4 * (random.random() + 1))
extra_radius = math.tan(math.pi/2 * random.random())
points_array = []
for i in range(30):
    theta = random.random() * math.pi
    phi = random.random() * 2*math.pi
    point_radius = (radius) * random.random()
    x = point_radius * math.sin(theta) * math.cos(phi) + x_center
    y = point_radius * math.sin(theta) * math.sin(phi) + y_center
    z = point_radius * math.cos(theta) + z_center
    points_array.append((x, y, z))
for i in range(4):
    theta = random.random() * math.pi
    phi = random.random() * 2 * math.pi
    x = (radius) * math.sin(theta) * math.cos(phi) + x_center
    y = (radius) * math.sin(theta) * math.sin(phi) + y_center
    z = (radius) * math.cos(theta) + z_center
    #print(format((x, y, z)))
    points_array.append((x, y, z))
for i in range(3):
    theta = random.random() * math.pi
    phi = random.random() * 2 * math.pi
    x = (radius + extra_radius) * math.sin(theta) * math.cos(phi) + x_center
    y = (radius + extra_radius) * math.sin(theta) * math.sin(phi) + y_center
    z = (radius + extra_radius) * math.cos(theta) + z_center
    #print(format((x, y, z)))
    points_array.append((x, y, z))
    #print(format((x, y, z)))
#print("Points array: " + format(points_array))
print("Inner radius is: " + format(radius))
print("Total radius is: " + format(radius + extra_radius))
print("Actual center is at (" + format(x_center) + ", " + format(y_center) + ", " + format(z_center) + ")")
sphere_produced = PermissiveFindSmallestSphere4Points.main(points_array, .1)
print("Inner radius is: " + format(radius))
print("Total radius is: " + format(radius + extra_radius))
print("Actual center is at (" + format(x_center) + ", " + format(y_center) + ", " + format(z_center) + ")")
print("Calculated radius is: " + format(sphere_produced[0]))
print("Calculated center is: " + format(sphere_produced[1]))