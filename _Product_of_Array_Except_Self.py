n=int(input())
x=list(map(int,input().split()))
f=1
l=[]
for i in x:
    f*=i
for i in x:
    j=f//i
    l.append(j)
print(*l)