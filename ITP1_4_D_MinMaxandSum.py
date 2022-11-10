n = int(input())
n_list = list(map(int, input().split()))
mi = n_list[0]
ma = n_list[0] 
su = 0
for i in range(n):
    if mi > n_list[i]:
        mi = n_list[i]
    if ma < n_list[i]:
        ma = n_list[i]
    su+=n_list[i]

print(str(mi)+' '+str(ma)+' '+str(su))