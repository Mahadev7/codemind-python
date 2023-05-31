n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
for i in x:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
s=[]
while True:
    if len(a)==0 and len(b)==0:
        break
    elif len(a)==0:
        s.append(b[0])
        b.pop(0)
    elif len(b)==0:
        s.append(a[0])
        a.pop(0)
    else:
        s.append(a[0])
        s.append(b[0])
        a.pop(0)
        b.pop(0)
if len(s)%2!=0:
    s.append(0)
print(*s)