# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:13:25 2021

@author: Peter
"""

import sys
import CenterFrom3Points3DScript
import random
import numpy as np
import math
def distance(Ax, Ay, Az, Bx, By, Bz):
    return math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By) + (Az-Bz)*(Az-Bz))

XCenter = math.tan(math.pi/4 * (random.random() + 1))
YCenter = math.tan(math.pi/4 * (random.random() + 1))
ZCenter = math.tan(math.pi/4 * (random.random() + 1))
Radius = math.tan(math.pi/4 * (random.random() + 1))
Alpha = random.random() * 2 * math.pi
#Alpha = 1.5 * math.pi
#Setting Alpha to 0, .5pi, pi, 1.5pi, or 2pi fixes everything, 
#makes everything work!
#However, it is not a truly good test if we throw away one axis
#of rotation, so we must find a way to fix the manner in which we
#construct the rotation matrix!
Beta = random.random() * 2 * math.pi
Gamma = random.random() * 2 * math.pi
AAngle = random.random() * 2 * math.pi
BAngle = random.random() * 2 * math.pi
CAngle = random.random() * 2 * math.pi
A = np.vstack([Radius * math.cos(AAngle), Radius * math.sin(AAngle), 0])
B = np.vstack([Radius * math.cos(BAngle), Radius * math.sin(BAngle), 0])
C = np.vstack([Radius * math.cos(CAngle), Radius * math.sin(CAngle), 0])
rot_matrix_yaw = [[math.cos(Alpha), -1 * math.sin(Alpha), 0],
                  [math.sin(Alpha), math.cos(Alpha), 0],
                  [0, 0, 1]]
rot_matrix_pitch = [[math.cos(Beta), 0, math.sin(Beta)],
                    [0, 1, 0],
                    [-1 * math.sin(Beta), 0, math.cos(Beta)]]
rot_matrix_roll = [[1, 0, 0],
                   [0, math.cos(Gamma), -1 * math.sin(Gamma)],
                   [0, math.sin(Gamma), math.cos(Gamma)]]
RotMatrix = np.matmul(np.matmul(rot_matrix_yaw, rot_matrix_pitch), rot_matrix_roll)
# RotMatrix = [[math.cos(Alpha)*math.cos(Beta), (math.cos(Alpha)*math.sin(Beta)*math.sin(Gamma)) - (math.sin(Alpha)*math.cos(Gamma)), (math.cos(Alpha)*math.sin(Beta)*math.cos(Gamma)) + (math.sin(Alpha)*math.sin(Gamma))],
#               [math.sin(Alpha)*math.cos(Beta), (math.sin(Alpha)*math.sin(Beta)*math.sin(Gamma)) - (math.cos(Alpha)*math.cos(Gamma)), (math.sin(Alpha)*math.sin(Beta)*math.cos(Gamma)) - (math.cos(Alpha)*math.sin(Gamma))],
#               [-math.sin(Beta), math.cos(Beta)*math.sin(Gamma), math.cos(Beta)*math.cos(Gamma)]]
# rot_matrix_transpose = np.transpose(RotMatrix)
# print("Determinant: " + format(np.linalg.det(RotMatrix)))
# print("Mult'd by transpose: " + format(np.matmul(RotMatrix, rot_matrix_transpose)))
APrime = np.matmul(RotMatrix, A)
BPrime = np.matmul(RotMatrix, B)
CPrime = np.matmul(RotMatrix, C)
print("Alpha: " + format(Alpha)+" Beta: " + format(Beta) + " Gamma: " + format(Gamma))
#print(format(RotMatrix))
#Radius = math.tan(math.pi/2 * random.random)
#Commented out version has a fuller range of numbers, but wanted
#to constrain it to higher values
print("Actual radius is " + format(Radius))
print("Actual center is at (" + format(XCenter) + ", " + format(YCenter) + ", " + format(ZCenter) + ")")
# print("Point A is actually at :" + format(APrime) + "\n And is rotated from :\n" + format(A))
# print("Point B is actually at :" + format(BPrime) + "\n And is rotated from :\n" + format(B))
# print("Point C is actually at :" + format(CPrime) + "\n And is rotated from :\n" + format(C))
# print("Distance between original A and B: " + format(distance(A[0][0], A[1][0], A[2][0], B[0][0], B[1][0], B[2][0])))
# print("Distance between rotated A and B: " + format(distance(APrime[0][0], APrime[1][0], APrime[2][0], BPrime[0][0], BPrime[1][0], BPrime[2][0])))
# print("A' Radius: :" + format(distance(APrime[0][0],APrime[1][0], APrime[2][0], 0, 0, 0)))
# print("B' Radius: :" + format(distance(BPrime[0][0],BPrime[1][0], BPrime[2][0], 0, 0, 0)))
# print("C' Radius: :" + format(distance(CPrime[0][0],CPrime[1][0], CPrime[2][0], 0, 0, 0)))
# print("A Radius: :" + format(distance(A[0][0],A[1][0], A[2][0], 0, 0, 0)))
# print("B Radius: :" + format(distance(B[0][0],B[1][0], B[2][0], 0, 0, 0)))
# print("C Radius: :" + format(distance(C[0][0],C[1][0], C[2][0], 0, 0, 0)))
CalcCenter = CenterFrom3Points3DScript.main(APrime[0][0] + XCenter, APrime[1][0] + YCenter, APrime[2][0] + ZCenter, BPrime[0][0] + XCenter, BPrime[1][0] + YCenter, BPrime[2][0] + ZCenter, CPrime[0][0] + XCenter, CPrime[1][0] + YCenter, CPrime[2][0] + ZCenter)
print("Calculated Center is at (" + format(CalcCenter[0]) + ", " + format(CalcCenter[1]) + ", " + format(CalcCenter[2]))
#print("Calculated Center is at " + format(CalcCenter))