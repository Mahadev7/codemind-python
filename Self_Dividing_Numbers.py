def seldiv(n):
    t=n
    while t:
        d=t%10
        t=t//10
        if d==0 or n%d!=0:
            return False
    return True
x=int(input())
y=int(input())
for i in range(x,y+1):
    if seldiv(i):#1
        print(i,end=" ")