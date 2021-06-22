# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:13:25 2021

@author: Peter
"""

import sys
import CenterFrom4Points3DScript
import random
import numpy as np
import math

Radius = math.tan(math.pi/4 * (random.random() + 1))
#Radius = math.tan(math.pi/2 * random.random)
#Commented out version has a fuller range of numbers, but wanted
#to constrain it to higher values
XCenter = math.tan(math.pi/4 * (random.random() + 1))
YCenter = math.tan(math.pi/4 * (random.random() + 1))
ZCenter = math.tan(math.pi/4 * (random.random() + 1))
ThetaA = random.random() * math.pi
PhiA = random.random() * 2*math.pi
ThetaB = random.random() * math.pi
PhiB = random.random() * 2*math.pi
ThetaC = random.random() * math.pi
PhiC = random.random() * 2*math.pi
ThetaD = random.random() * math.pi
PhiD = random.random() * 2*math.pi
Ax = Radius * math.sin(ThetaA) * math.cos(PhiA) + XCenter
Ay = Radius * math.sin(ThetaA) * math.sin(PhiA) + YCenter
Az = Radius * math.cos(ThetaA) + ZCenter
Bx = Radius * math.sin(ThetaB) * math.cos(PhiB) + XCenter
By = Radius * math.sin(ThetaB) * math.sin(PhiB) + YCenter
Bz = Radius * math.cos(ThetaB) + ZCenter
Cx = Radius * math.sin(ThetaC) * math.cos(PhiC) + XCenter
Cy = Radius * math.sin(ThetaC) * math.sin(PhiC) + YCenter
Cz = Radius * math.cos(ThetaC) + ZCenter
Dx = Radius * math.sin(ThetaD) * math.cos(PhiD) + XCenter
Dy = Radius * math.sin(ThetaD) * math.sin(PhiD) + YCenter
Dz = Radius * math.cos(ThetaD) + ZCenter
print("Actual radius is " + format(Radius))
print("Actual center is at (" + format(XCenter) + ", " + format(YCenter) + ", " + format(ZCenter) + ")")
#print("Point A is actually at (" + format(Ax) + ", " + format(Ay) + ", " + format(Az) + ")")
#print("Point B is actually at (" + format(Bx) + ", " + format(By) + ", " + format(Bz) + ")")
#print("Point C is actually at (" + format(Cx) + ", " + format(Cy) + ", " + format(Cz) + ")")
#print("Point D is actually at (" + format(Dx) + ", " + format(Dy) + ", " + format(Dz) + ")")
CalcCenter = CenterFrom4Points3DScript.main(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz, Dx, Dy, Dz)
print("Calculated Center is at (" + format(CalcCenter[0]) + ", " + format(CalcCenter[1]) + ", " + format(CalcCenter[2]))
print("Calculated Center is at " + format(CalcCenter))