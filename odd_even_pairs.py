n=int(input())
x=list(map(int,input().split()))
p1,p2=[],[]
for i in x:
    if i%2!=0:
        p1.append(i)
    else:
        p2.append(i)
l=[]
while True:
    if len(p1)==0 and len(p2)==0:
        break
    elif len(p1)==0:
        l.append(p2[0])
        p2.pop(0)
    elif len(p2)==0:
        l.append(p1[0])
        p1.pop(0)
    else:
        l.append(p1[0])
        l.append(p2[0])
        p1.pop(0)
        p2.pop(0)
if len(l)%2!=0:
    l.append(0)
print(*l)