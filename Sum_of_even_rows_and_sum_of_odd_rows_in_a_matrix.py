r,c=map(int,input().split())
m=[]
e=[]
o=[]
a=[]
b=[]
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
for i in range(r):
    if i%2==0:
        e.append(m[i])
    else:
        o.append(m[i])
for i in e:
    p=sum(i)
    a.append(p)
for i in o:
    q=sum(i)
    b.append(q)
print(sum(a),sum(b))