def palin(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
x=int(input())
a=x+1
b=x-1
while True:
    if palin(a) and palin(b):
        print(b,a)
        break
    if palin(a):
        print(a)
        break
    if palin(b):
        print(b)
        break
    a+=1
    b-=1