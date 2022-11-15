n,m = map(int, input().split())
a = []
b = []
c = []
for i in range(n):
    n_list = list(map(int, input().split()))
    a.append(n_list)

for j in range(m):
    b.append(int(input()))

cs = [[b[j]*a[i][j] for j in range(m)] for i in range(n)]
for i in range(n):
    c.append(sum(cs[i]))
for i in range(n):
    print(c[i])