m=int(input())
x=list(map(int,input().split()))
l,n=map(int,input().split())
a=[]
b=0
for i in x:
    if i>=l and i<=n:
        a.append(i)
        b=1
if b==0:
    print('-1')
else:
    print(max(a))