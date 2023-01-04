n=int(input())
x=list(map(int,input().split()))
k=int(input())
s=[]
c=0
for i in x:
    if k==x.count(i):
        s.append(i)
        c=1
        a=set(s)
if c==0:
    print("-1")
else:
    for i in a:
        print(i,end=" ")