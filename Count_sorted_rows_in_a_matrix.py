r,c=map(int,input().split())
m=[]
c=0
for i in range(r):
    x=list(map(int,input().split()))
    m.append(x)
for i in m:
    if sorted(i)==i or sorted(i,reverse=True)==i:
        c+=1
print(c)