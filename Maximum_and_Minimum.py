n=int(input())
x=list(map(int,input().split()))
s=[]
c=0
for i in x:
    if i==x.count(i):
        s.append(i)
        c=1
        a=set(s)#
        m=min(a)
        n=max(a)
if c==0:
    print("-1")
else:
    print(m,n)