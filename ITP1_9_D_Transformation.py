# Write a program which performs a sequence of commands to a given string str. The command is one of

commands_list=[]

word=input()
times=int(input())
print_count=0
prited_words=[]

for i in range(times):
    command=list(map(str,input().split()))
    commands_list.append(command)

for i in range(times):
    if commands_list[i][0]=='replace':
        word=rep(word,int(commands_list[i][1]),int(commands_list[i][2]),commands_list[i][3])
    elif commands_list[i][0]=='reverse':
        word=rev(word,int(commands_list[i][1]),int(commands_list[i][2]))
    else:
        printed_words.append(pri(word,int(commands_list[i][1]),int(commands_list[i][2])))
        print_count+=1

for i in range(print_count):
    print(printed_words[i])

