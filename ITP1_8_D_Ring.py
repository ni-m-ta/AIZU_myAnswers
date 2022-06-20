#Write a program which reads a word W and a text T, and prints the number of word W which appears in text T

w=input()
words_list=[]
count=0

while True:
    words=list(map(str,input().split()))
    if 'END_OF_TEXT' in words:
        break
    words_list+=words

for i in range(len(words_list)):
    if w==words_list[i].lower():
        count+=1

print(count)