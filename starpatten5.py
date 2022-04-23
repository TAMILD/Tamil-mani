n=int(input())
for i in range(n):
    tp=0
    for j in range(n):
        if i+j>=n-1:
            tp=+1
            print(tp,end=" ")
        else:
            print(' ',end=" ")
    for j in range(1,n):
        if i>=j:
            tp-=1
            print(tp,end=" ")
        else:
            print(' ',end=" ") 
    print()