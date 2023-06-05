n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
l=[]
while True:
    if len(y)==1:
        l.append(y[0])
        break
    else:
        l.append(y[-2])
        l.append(y[-1])
        y.pop(-2)
        y.pop(-1)
    if len(y)==0:
        break
print(*l)