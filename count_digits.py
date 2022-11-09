n=int(input())
x=list(map(str,input().split()))
for i in range(n):
    s=len(x[i])
    if int(x[i])<0:
        s-=1
    print(s,end=" ")