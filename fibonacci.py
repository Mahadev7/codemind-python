a=int(input())
x=0
y=1
c=0
while c<a:
    print(x,end=' ')
    t=x+y
    x=y
    y=t
    c+=1