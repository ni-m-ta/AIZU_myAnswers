ns_list = []
while True:
    n_list = list(map(str, input().split()))
    if n_list[1] == '?':
        break
    ns_list.append(n_list)

for i in range(len(ns_list)):
    if ns_list[i][1] == '+':
        print(int(ns_list[i][0])+int(ns_list[i][2]))
    elif ns_list[i][1] == '-':
        print(int(ns_list[i][0])-int(ns_list[i][2]))
    elif ns_list[i][1] == '*':
        print(int(ns_list[i][0])*int(ns_list[i][2]))
    else:
        print(int(ns_list[i][0])//int(ns_list[i][2]))