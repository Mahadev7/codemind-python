n,k=map(int,input().split())
x=list(map(int,input().split()))
l=[]
for i in range(len(x)):
    for j in range(i,len(x)):
        s=x[i:j+1]
        l.append(s)
# print(l)
c=0
for i in l:
    s=sum(i)
    if s==k:
        c+=1
print(c)