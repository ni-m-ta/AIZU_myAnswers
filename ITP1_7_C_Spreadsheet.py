import sys
input = sys.stdin.readline
nums = []
sum_r = []
r,c = map(int, input().split())
for j in range(r):
    col = list(map(int, input().split()))
    col.append(sum(col))
    nums.append(col)

for i in range(c+1):
    temp = 0
    for j in range(r):
        temp += nums[j][i]
    sum_r.append(temp)
nums.append(sum_r)

for j in range(r+1):
    for i in range(c+1):
        if i == c:
            print(nums[j][i])
        else:
            print(nums[j][i],end=' ')


