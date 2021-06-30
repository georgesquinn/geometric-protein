# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:37:43 2021

@author: Peter
"""
import FindSmallestSphere2Points
import FindSmallestSphere3Points
import FindSmallestSphere4Points


def main(points_array):
    two_p_sphere = FindSmallestSphere2Points.main(points_array)
    if two_p_sphere is not None:
        print("Two point sphere")
        return two_p_sphere
    three_p_sphere = FindSmallestSphere3Points.main(points_array)
    if three_p_sphere[0] is not None and three_p_sphere[2]:
        print("Three point sphere")
        return three_p_sphere
    print("Four point sphere")
    four_p_sphere = FindSmallestSphere4Points.main(points_array)
    # if (three_p_sphere != None):
    #     print("Three Radius:" + format(three_p_sphere[0]))
    #     print("Three status: " + format(three_p_sphere[2]))
    #     print("Four Radius: " + format(four_p_sphere[0]))
    # if (three_p_sphere[0] != None and three_p_sphere[0] < four_p_sphere[0]):
    #     return three_p_sphere
    return four_p_sphere
