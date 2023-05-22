n=int(input())
x=list(map(int,input().split()))
a=[]
c=0
for i in x:
    if i==x.count(i):
        c+=1
        a.append(i)
s=set(a)
if sum(s)==0:
    avg=0
else:
    avg=sum(s)/len(s)
if c==0:
    print('-1')
else:
    print("%.2f"%avg)