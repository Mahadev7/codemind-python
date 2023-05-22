n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
c=0
for i in x:
    if i==x.count(i):
        a.append(i)
        c=1
for i in a:
    if i not in b:
        b.append(i)
if c==0:
    print('-1')
else:
    for i in b:
        print(i,end=' ')