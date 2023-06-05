n=int(input())
x=list(map(int,input().split()))
x=set(x)
p=[]
for i in x:
    p.append(i)
m=sorted(p,reverse=True)
if len(m)>=3:
    print(m[2])
else:
    print(max(m))