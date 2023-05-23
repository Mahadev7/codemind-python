r,c=map(int,input().split())
x=[]
s=0
for i in range(r):
    y=list(map(int,input().split()))
    x.append(y)
    s+=sum(y)
print(s)