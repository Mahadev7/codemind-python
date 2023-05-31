r,c=map(int,input().split())
m=[]
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
s=0
for i in range(r):
    if i==r-1-i:
        s+=m[i][i]
    else:
        s+=m[i][i]
        s+=m[i][r-1-i]
print(s)