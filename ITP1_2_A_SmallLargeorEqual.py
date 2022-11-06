a,b = map(int, input().split())
if a < b:
    sign = ' < '
elif a == b:
    sign = ' == '
else:
    sign = ' > '
print('a'+sign+'b')
