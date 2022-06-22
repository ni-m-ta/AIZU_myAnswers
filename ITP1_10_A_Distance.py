#Write a program which calculates the distance between two points P1(x1, y1) and P2(x2, y2).
import math

x1,y1,x2,y2=map(float,input().split())

dis=math.sqrt((x1-x2)**2+(y1-y2)**2)

print(dis)