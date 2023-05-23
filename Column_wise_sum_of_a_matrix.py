r,c=map(int,input().split())
m=[]
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
for i in range(c):
    s=0
    for j in range(r):
        s+=m[j][i]
    print(s,end=' ')