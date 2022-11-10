count = int(input())
n_list = list(map(int, input().split()))

for i in range(count):
    if i == count-1:
        print(str(n_list[0]))
    else:
        print(str(n_list[count-i-1])+' ',end='')
