def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
x=int(input())
a=x+1
b=x-1
while 1:
    if isprime(x):
        print(0)
        break
    if isprime(a) and isprime(b):
        x1=abs(x-a)
        y1=abs(x-b)
        print(min(x1,y1))
        break
    if isprime(a):
        print(abs(a-x))
        break
    if isprime(b):
        print(abs(b-x))
        break
    a+=1
    b-=1