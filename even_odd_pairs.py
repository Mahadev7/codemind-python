n=int(input())
x=list(map(int,input().split()))
m=[]
n=[]
for i in x:
    if i%2==0:
        m.append(i)
    else:
        n.append(i)
a=[]
while True:
    if len(m)==0 and len(n)==0:
        break
    elif len(m)==0:
        a.append(n[0])
        n.pop(0)
    elif len(n)==0:
        a.append(m[0])
        m.pop(0)
    else:
        a.append(m[0])
        a.append(n[0])
        m.pop(0)
        n.pop(0)
if len(a)%2!=0:
    a.append(0)
print(*a)