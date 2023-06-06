def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for i in range(int(input())):
    x=int(input())
    a=x+1
    b=x-1
    while True:
        if prime(x):
            print(x)
            break
        if prime(a) and prime(b):
            print(min(a,b))
            break
        if prime(a):
            print(a)
            break
        if prime(b):
            print(b)
            break
        a+=1
        b-=1