ns_list = []
while True:
    n_list = list(map(int, input().split()))
    if 0 == n_list[0] and 0 == n_list[1]:
        break
    n_list.sort()
    ns_list.append(n_list)

for i in range(len(ns_list)):
    print(str(ns_list[i][0])+' '+str(ns_list[i][1]))

