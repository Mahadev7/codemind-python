def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for i in range(int(input())):
    a=int(input())
    x=a+1
    y=a-1
    while 1:
        if prime(a):
            print(a)
            break
        if prime(x) and prime(y):
            print(min(x,y))
            break
        if prime(x):
            print(x)
            break
        if prime(y):
            print(y)
            break
        x+=1
        y-=1