# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:37:43 2021

@author: Peter
"""
import FindSmallestSphere2Points
import FindSmallestSphere3Points
import FindSmallestSphere4Points

def main(PointsArray):
    TwoPSphere = FindSmallestSphere2Points.main(PointsArray)
    if TwoPSphere != None:
        return TwoPSphere
    ThreePSphere = FindSmallestSphere3Points.main(PointsArray)
    if (ThreePSphere[0] != None and ThreePSphere[2] == True):
        return ThreePSphere
    FourPSphere = FindSmallestSphere4Points.main(PointsArray)
    # if (ThreePSphere != None):
    #     print("Three Radius:" + format(ThreePSphere[0]))
    #     print("Three status: " + format(ThreePSphere[2]))
    #     print("Four Radius: " + format(FourPSphere[0]))
    # if (ThreePSphere[0] != None and ThreePSphere[0] < FourPSphere[0]):
    #     return ThreePSphere
    return FourPSphere