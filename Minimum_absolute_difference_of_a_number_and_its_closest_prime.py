def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
a=n+1
b=n-1
while True:
    if prime(n):
        print(0)
        break
    if prime(a) and prime(b):
        x=abs(a-n)
        y=abs(b-n)
        print(min(x,y))
        break
    if prime(a):
        print(abs(n-a))
        break
    if prime(b):
        print(abs(n-b))
        break
    a+=1
    b-=1