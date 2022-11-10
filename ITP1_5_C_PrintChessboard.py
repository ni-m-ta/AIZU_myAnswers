ns_list = []
while True:
    n_list = list(map(int, input().split()))
    if n_list[0] == 0 and n_list[1] == 0:
        break
    ns_list.append(n_list)

for i in range(len(ns_list)):
    for ii in range(ns_list[i][0]):
        if ii%2 == 0:
            for iii in range(ns_list[i][1]):
                if iii%2 == 0:
                    if iii == ns_list[i][1]-1:
                        print('#')
                    else:
                        print('#',end='')
                else:
                    if iii == ns_list[i][1]-1:
                        print('.')
                    else:
                        print('.',end='')
        else:
            for iii in range(ns_list[i][1]):
                if iii%2 == 0:
                    if iii == ns_list[i][1]-1:
                        print('.')
                    else:
                        print('.',end='')
                else:
                    if iii == ns_list[i][1]-1:
                        print('#')
                    else:
                        print('#',end='')                
    print()