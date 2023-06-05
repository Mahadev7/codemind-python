n=int(input())
x=list(map(int,input().split()))
x=set(x)
l=[]
for i in x:
    l.append(i)
l1=sorted(l,reverse=True)
# print(l)
if len(l1)>=3:
    print(l1[2])
else:
    print(max(l1))