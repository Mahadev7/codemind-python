n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=0
for i in x:
    if i>=a and i<=b:
        c.append(i)
        d=1
if d==0:
    print('-1')
else:
    print(min(c))