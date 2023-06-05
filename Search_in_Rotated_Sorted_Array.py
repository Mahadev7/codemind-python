n=int(input())
x=list(map(int,input().split()))
m=int(input())
p=[]
for i in range(n):
    if x[i]==m:
        p.append(i)
if len(p)==0:
    print(-1)
else:
    print(*p)