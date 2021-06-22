# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:47:29 2021

@author: Peter
"""
import numpy as np
def main(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    #Method created by Avinash
    CircNormVec = [((By - Ay)*(Cz - Az) - (Bz - Az)*(Cy - Ay)),
                   ((Bz - Az)*(Cx - Ax) - (Bx - Ax)*(Cz - Az)),
                   ((Bx - Ax)*(Cy - Ay) - (By - Ay)*(Cx - Ax)),]
    #CircNormVecX = (By - Ay)*(Cz - Az) - (Bz - Az)*(Cy - Ay)
    #CircNormVecY = (Bz - Az)*(Cx - Ax) - (Bx - Ax)*(Cz - Az)
    #CircNormVecZ = (Bx - Ax)*(Cy - Ay) - (By - Ay)*(Cx - Ax)
    #A = np.array([[(Bx - Ax), (By - Ay), (Bz - Az)], [(Cx - Ax), (Cy - Ay), (Cz - Az)], CircNormVec], dtype=float)
    A = np.array([[Bx - Ax, By - Ay, Bz - Az,], 
                  [Cx - Ax, Cy - Ay, Cz - Az,], 
                  CircNormVec])
   # print(format(A))
    Ainv = np.linalg.inv(A)
    #print(format(Ainv))
    PA = ((Ax*Ax + Ay*Ay + Az*Az))
    PB = ((Bx*Bx + By*By + Bz*Bz))
    PC = ((Cx*Cx + Cy*Cy + Cz*Cz))
    DotProd = (CircNormVec[0]*Ax+ CircNormVec[1]*Ay+ CircNormVec[2]*Az)
    PMatrix = np.array([((PB - PA)/2), ((PC - PA)/2), (DotProd)])
    #print(format(PMatrix))
    Result = np.matmul(Ainv, PMatrix)
    return Result
    
    