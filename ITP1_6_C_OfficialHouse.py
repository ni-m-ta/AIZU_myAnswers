n = int(input())
buils = []
for i in range(n):
    buil = list(map(int, input().split()))
    buils.append(buil)

for i in range(1,5):
    for ii in range(1,4):
        for iii in range(1,11):
            if iii == 10:
                print('0')
            else:
                print('0',end=' ')
    if i != 4:
        print('#'*20)                 
                            

                        


                

