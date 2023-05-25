r,c=map(int,input().split())
m=[]
p=[]
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
for i in range(r):
    s=0
    for j in range(c):
        s+=m[i][j]
        p.append(s)
print(max(p))