
import sys

def slope(Ax, Ay, Bx, By):
    if Ax > Bx:
        Cx = Bx
        Cy = By
        Bx = Ax
        By = Ay
        Ax = Cx
        Ay = Cy
    ans = (By - Ay) / (Bx - Ax)
    return ans


Aax = sys.argv[1]
Aay = sys.argv[2]
Bbx = sys.argv[3]
Bby = sys.argv[4]
Ccx = sys.argv[5]
Ccy = sys.argv[6]
#Aax = 7.2
#Aay = -33.998
#Bbx = 11.83
#Bby = -32.998
#Ccx = 10.46
#Ccy = -34.141
Slope1 = slope(Aax, Aay, Bbx, Bby)
NRslope1 = -1/Slope1
Midpoint1x = (Aax + Bbx)/2
Midpoint1y = (Aay + Bby)/2
Slope2 = slope(Bbx, Bby, Ccx, Ccy)
NRslope2 = -1/Slope2
Midpoint2x = (Bbx + Ccx)/2
Midpoint2y = (Bby + Ccy)/2
Intercept1 = Midpoint1y - (NRslope1*Midpoint1x)
Intercept2 = Midpoint2y - (NRslope2*Midpoint2x)
A = NRslope1
B = Intercept1
C = NRslope2
D = Intercept2
print('Line 1 is ' + format(A) +'x + ' + format(B))
print('Line 2 is ' + format(C) +'x + ' + format(D))
FinalX = (D - B)/(A-C)
FinalY = A*FinalX + B
print('The circle is centered at ' + format(FinalX) + ' , ' + format(FinalY))
Result = (FinalX, FinalY)
return Result


    
