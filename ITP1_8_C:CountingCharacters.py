#Write a program which counts and reports the number of each alphabetical letter. Ignore the case of characters.

import sys
array=[]
count_list=[0]*26
for line in sys.stdin.readlines():
	array.append(line.rstrip())

for i in range(len(array)):
    for ii in range(len(array[i])):
        for n in range(len(count_list)):
            if n+97==ord(array[i][ii]) or n+97-32==ord(array[i][ii]):
                count_list[n]+=1

for i in range(len(count_list)):
    print(chr(i+97)+' : '+str(count_list[i]))


