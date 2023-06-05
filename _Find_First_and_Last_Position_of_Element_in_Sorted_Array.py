a=int(input())
p=[]
x=list(map(int,input().split()))
n=int(input())
for i in range(a):
    if x[i]==n:
        p.append(i)
if len(p)==0:
    p.append(-1)
    p.append(-1)
elif len(p)==1:
    p.append(p[0])
l=[]
if len(p)>2:
    l.append(p[0])
    l.append(p[-1])
if len(p)>2:
    print(*l)
else:
    print(*p)
    