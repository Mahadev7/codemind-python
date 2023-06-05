n=int(input())
x=list(map(int,input().split()))
b=sorted(x)
p=[]
while True:
    if len(b)==1:
        p.append(b[0])
        break
    else:
        p.append(b[-2])
        p.append(b[-1])
        b.pop(-2)
        b.pop(-1)
    if len(b)==0:
        break
print(*p)