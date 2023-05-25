n,m=map(int,input().split())
a=[]
c=0
for i in range(n):
    x=list(map(int,input().split()))
    a.append(x)
for i in  a:
    if sorted(i)==i or sorted(i,reverse=True)==i:
        c+=1
print(c)