r,c=map(int,input().split())
m=[]
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
for i in range(r):
    s=0
    for j in range(c):
        s+=m[i][j]
    print(s,end=" ")