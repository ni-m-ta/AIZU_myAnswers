n_list = []
i = 0
while True:
    n = int(input())
    if n == 0:
        break
    n_list.append(n)

for i in range(len(n_list)):
    print('Case '+str(i+1)+': '+str(n_list[i]))