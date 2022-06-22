#For given two sides of a triangle a and b and the angle C between them, calculate the following properties:

import math
import decimal

a,b,c=map(float,input().split())

s=1/2*a*b*math.sin(math.radians(c))

l=a+b+(math.sin(math.radians(c))*a)

h=s*2/a

print(s)
print(l)
print(h)