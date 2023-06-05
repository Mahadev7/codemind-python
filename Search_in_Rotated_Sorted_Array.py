n=int(input())
x=list(map(int,input().split()))
a=int(input())
l=[]
for i in range(n):
    if x[i]==a:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(*l)