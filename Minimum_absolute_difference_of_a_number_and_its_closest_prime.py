def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
x=n+1
y=n-1
while True:
    if prime(n):
        print(0)
        break
    if prime(x) and prime(y):
        a=abs(x-n)
        b=abs(y-n)
        print(min(a,b))
        break
    if prime(x):
        print(abs(x-n))
        break
    if prime(y):
        print(abs(y-n))
        break
    x+=1
    y-=1