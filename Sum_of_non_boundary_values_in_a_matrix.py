r,c=map(int,input().split())
m=[]
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
p=0
for i in range(1,r-1):
    for j in range(1,c-1):
        p+=m[i][j]
print(p)