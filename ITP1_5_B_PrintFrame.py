ns_list = []
while True:
    n_list = list(map(int, input().split()))
    if n_list[0] == 0 and n_list[1] == 0:
        break
    ns_list.append(n_list)

for i in range(len(ns_list)):
    for ii in range(ns_list[i][0]):
        if ii == 0 or ii == (ns_list[i][0]-1):
            print('#'*ns_list[i][1])
        else:
            print('#'+'.'*(ns_list[i][1]-2)+'#')
    print('')
