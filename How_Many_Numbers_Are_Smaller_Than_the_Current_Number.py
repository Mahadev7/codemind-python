n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in x:
        if x[i]>j:
            c+=1
    print(c,end=' ')