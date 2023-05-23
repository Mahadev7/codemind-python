r,c=map(int,input().split())
s=0
for i in range(r):
    x=list(map(int,input().split()))
    s+=sum(x)
print(s)