n = int(input())
cs_list = []
for i in range(n):
    c_list = list(map(str, input().split()))
    cs_list.append(c_list)

all_cards = []
for i in range(4):
    if i == 0:
        for ii in range(1,14):
            all_cards.append(['C',str(ii)])
    elif i == 1:
         for ii in range(1,14):
            all_cards.append(['D',str(ii)])
    elif i == 2:
         for ii in range(1,14):
            all_cards.append(['H',str(ii)])
    else:
         for ii in range(1,14):
            all_cards.append(['S',str(ii)])

diff_list = []
for card in all_cards:
    if card not in cs_list:
        diff_list.append(card)

for i in range(len(diff_list)):
    print(diff_list[i][0]+' '+diff_list[i][1])