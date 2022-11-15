import sys
imput = sys.stdin.readline
n,m,l = map(int, input().split())
a = [list(map(int,input().split())) for i in range(n)]
b = [list(map(int,input().split())) for k in range(m)]
c = [[0 for j in range(l)] for i in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]

for i in range(n):
    for j in range(l):
        if j == l-1:
            print(c[i][j])
        else:
            print(c[i][j],end=' ')