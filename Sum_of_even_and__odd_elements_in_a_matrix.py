r,c=map(int,input().split())
m=[]
s=0
s1=0
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
for i in range(r):
    for j in range(c):
        if m[i][j]%2==0:
            s+=m[i][j]
        else:
            s1+=m[i][j]
print(s,s1)