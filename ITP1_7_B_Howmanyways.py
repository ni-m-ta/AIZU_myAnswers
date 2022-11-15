import sys
input = sys.stdin.readline
counts = []
while True:
    n,x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i+1)+(j+1)+(k+1) == x and i < j and j < k:
                    count += 1
    counts.append(count)

for count in counts:
    print(count)
                
            
