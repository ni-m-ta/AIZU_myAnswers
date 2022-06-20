#Your task is to shuffle a deck of n cards, each of which is marked by a alphabetical letter.

words_list=[]
num_list=[]
shuffle_list=[]

while True:
    tmpnum_list=[]
    word=input()
    if word=='-':
        break
    num=int(input())
    words_list.append(word)
    num_list.append(num)
    for i in range(num):
        tmpnum_list.append(int(input()))
    shuffle_list.append(tmpnum_list)

for i in range(len(words_list)):
    print(words_list[i])
    print(num_list[i])
    print(shuffle_list[i])