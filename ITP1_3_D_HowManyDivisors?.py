a,b,c = map(int, input().split())
count = 0
for i in range(a, b+1):
    if 0 == (c%i):
        count+=1
print(count)
