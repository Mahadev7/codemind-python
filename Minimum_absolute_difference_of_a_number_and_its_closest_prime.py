def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


n=int(input())
x=n+1
y=n-1
while 1:
    if isprime(n):
        print(0)
        break
    if isprime(x) and isprime(y):
        c=abs(n-x)
        d=abs(n-y)
        print(min(c,d))
        break
    if isprime(x):
        print(abs(n-x))
        break
    if isprime(y):
        print(abs(n-y))
        break
    x+=1
    y-=1
    