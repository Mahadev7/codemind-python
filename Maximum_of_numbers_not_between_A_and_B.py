n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
a1=0
for i in range(n):
    if x[i]<a or x[i]>b:
        c.append(x[i])
        a1=1
if a1==0:
    print('-1')
else:
    print(max(c))