# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:04:49 2021

@author: Peter
"""

import math
import numpy as np
import FindSmallestSphere2Points
import random

def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By) + (Az-Bz)*(Az-Bz))


x_center = math.tan(math.pi/4 * (random.random() + 1))
y_center = math.tan(math.pi/4 * (random.random() + 1))
z_center = math.tan(math.pi/4 * (random.random() + 1))
radius = math.tan(math.pi/4 * (random.random() + 1))
extra_radius = math.tan(math.pi/2 * random.random())
points_array = []
for i in range(500):
    theta = random.random() * math.pi
    phi = random.random() * 2*math.pi
    point_radius = (radius + extra_radius) * random.random()
    x = point_radius * math.sin(theta) * math.cos(phi) + x_center
    y = point_radius * math.sin(theta) * math.sin(phi) + y_center
    z = point_radius * math.cos(theta) + z_center
    points_array.append((x, y, z))
for i in range(100):
    theta = random.random() * math.pi
    phi = random.random() * 2 * math.pi
    x = (radius + extra_radius * .999) * math.sin(theta) * math.cos(phi) + x_center
    y = (radius + extra_radius * .999) * math.sin(theta) * math.sin(phi) + y_center
    z = (radius + extra_radius * .999) * math.cos(theta) + z_center
    points_array.append((x, y, z))
    #print(format((x, y, z)))
#print("Points array: " + format(points_array))
theta_one = random.random() * math.pi
phi_one = random.random() * math.pi * 2
#phi_one = math.pi
x_one = ((radius + extra_radius) * math.sin(theta_one) * math.cos(phi_one)) + x_center
y_one = ((radius + extra_radius) * math.sin(theta_one) * math.sin(phi_one)) + y_center
z_one = ((radius + extra_radius) * math.cos(theta_one)) + z_center
#theta_two = ((theta_one - math.pi/2) * -1) + math.pi/2 
theta_two = math.pi - theta_one
#phi_two = ((phi_one - math.pi) * -1) + math.pi
phi_two = (phi_one + math.pi)
x_two = ((x_one - x_center) * -1) + x_center
y_two = ((y_one - y_center) * -1) + y_center
z_two = ((z_one - z_center) * -1) + z_center
# x_two = ((radius + extra_radius) * math.sin(theta_two) * math.cos(phi_two)) + x_center
# y_two = ((radius + extra_radius) * math.sin(theta_two) * math.sin(phi_two)) + y_center
# z_two = ((radius + extra_radius) + math.cos(theta_two)) + z_center
points_array.append((x_one, y_one, z_one))
points_array.append((x_two, y_two, z_two))
#print("Theta one: " + format(theta_one / math.pi))
#print("Theta two: " + format(theta_two / math.pi))
#print("Phi one: " + format(phi_one / math.pi))
#print("Phi two: " + format(phi_two / math.pi))
print("Inner radius is: " + format(radius))
print("Total radius is: " + format(radius + extra_radius))
print("Actual center is at (" + format(x_center) + ", " + format(y_center) + ", " + format(z_center) + ")")
#print("Distance between 2 extremes is: " + format(distance(x_one, y_one, z_one, x_two, y_two, z_two)))
sphere_produced = FindSmallestSphere2Points.main(points_array)
print("Calculated radius is: " + format(sphere_produced[0]))
print("Calculated center is: " + format(sphere_produced[1]))