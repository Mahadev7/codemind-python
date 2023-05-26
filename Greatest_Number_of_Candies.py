n=int(input())
x=list(map(int,input().split()))
k=int(input())
p=max(x)
for i in x:
    if (i+k)>=p:
        print("True",end=' ')
    else:
        print("False",end=' ')