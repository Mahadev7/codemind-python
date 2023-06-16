r,c=map(int,input().split())
m=[]
p,q=[],[]
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
for i in range(r):
    if i%2==0:
        p.append(m[i])
    else:
        q.append(m[i])
p1,q1=[],[]
for i in p:
    p1.append(sum(i))
for i in q:
    q1.append(sum(i))
print(sum(p1),sum(q1))