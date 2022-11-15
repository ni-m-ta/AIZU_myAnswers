scores = []
while True:
    m,f,r = map(int, input().split())
    if m == -1 and f == -1 and r ==-1:
        break
    elif m == -1 or f == -1:
        scores.append('F')      
    elif r == -1:
        if m+f >= 80:
            scores.append('A')
        elif m+f >= 65:
            scores.append('B')
        elif m+f >= 50:
            scores.append('C')
        elif m+f >= 30:
            scores.append('D')
        else:
            scores.append('F')
    else:
        if r >= 50:
            scores.append('C')
        elif r <= 50 and m+f >= 30:
            scores.append('D')
        else:
            scores.append('F')
    
for i in range(len(scores)):
    print(scores[i])
 
