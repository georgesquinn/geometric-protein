# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:37:43 2021

@author: Peter
"""
import PermissiveFindSmallestSphere2Points
import PermissiveFindSmallestSphere3Points
import PermissiveFindSmallestSphere4Points


def main(points_array, allowance_constant):
    two_p_sphere = PermissiveFindSmallestSphere2Points.main(points_array, allowance_constant)
    three_p_sphere = PermissiveFindSmallestSphere3Points.main(points_array, allowance_constant)
    four_p_sphere = PermissiveFindSmallestSphere4Points.main(points_array, allowance_constant)
    if two_p_sphere[0] < three_p_sphere[0] and two_p_sphere[0] < four_p_sphere[0]:
        return two_p_sphere
    if three_p_sphere[0] < four_p_sphere[0]:
        return three_p_sphere
    return four_p_sphere
