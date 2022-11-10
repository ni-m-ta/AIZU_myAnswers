W,H,x,y,r = map(int, input().split())
flag = "Yes"
if 0 > (x-r) or W < (x+r):
    flag = "No"
if 0 > (y-r) or H < (y+r):
    flag = "No"
print(flag)