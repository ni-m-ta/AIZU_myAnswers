import math
r = float(input())
area = r*r*math.pi
cir = 2*r*math.pi

print(str('{:.6f}'.format(area))+' '+str('{:.6f}'.format(cir)))