a,b,c=map(int, input().split())
if a > b:
    temp = b
    b = a
    a = temp
if a > c:
    temp = c
    c = a
    a = temp
if b > c:
    temp = b
    b = c
    c = temp
print(str(a)+' '+str(b)+' '+str(c))