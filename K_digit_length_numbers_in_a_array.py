n,k=map(int,input().split())
x=list(map(str,input().split()))
c = 0
for i in x:
    l=len(i)
    if int(i)<0:
        l-=1
    if l==k:
        c+=1
print(c)
    