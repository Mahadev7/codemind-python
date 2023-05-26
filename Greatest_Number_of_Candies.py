n=int(input())
x=list(map(int,input().split()))
k=int(input())
c=max(x)
for i in x:
    if (i+k)>=c:
        print("True",end=' ')
    else:
        print("False",end=' ')