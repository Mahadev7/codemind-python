def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(2,n):
    if n%i ==0 and prime(i):
        l.append(i)
if len(l)<2:
    print(-1)
else:
    print(*l)