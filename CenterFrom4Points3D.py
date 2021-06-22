
import sys
import numpy as np
import math
# Ax = sys.argv[1]
# Ay = sys.argv[2]
# Az = sys.argv[3]
# Bx = sys.argv[4]
# By = sys.argv[5]
# Bz = sys.argv[6]
# Cx = sys.argv[7]
# Cy = sys.argv[8]
# Cz = sys.argv[9]
# Dx = sys.argv[10]
# Dy = sys.argv[11]
# Dz = sys.argv[12]
Ax = 1
Ay = 1
Az = 1
Bx = -1
By = 1
Bz = 1
Cx = 1
Cy = -1
Cz = -1
Dx = -1
Dy = 1
Dz = -1

#Method created by Avinash
A = np.array([[Bx - Ax, By - Ay, Bz - Az,], 
              [Cx - Ax, Cy - Ay, Cz - Az,], 
              [Dx - Ax, Dy - Ay, Dz - Az]])
print(format(A))
Ainv = np.linalg.inv(A)
print(format(Ainv))
PA = Ax*Ax + Ay*Ay + Az*Az
PB = Bx*Bx + By*By + Bz*Bz
PC = Cx*Cx + Cy*Cy + Cz*Cz
PD = Dx*Dx + Dy*Dy + Dz*Dz
PMatrix = np.array([(PB-PA)/2, (PC-PA)/2, (PD-PA)/2])
print(format(PMatrix))
Result = np.matmul(Ainv, PMatrix)
print(format(Result))