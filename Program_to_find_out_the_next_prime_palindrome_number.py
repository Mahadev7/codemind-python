def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def palin(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
n=int(input())
b=n+1
while True:
    if prime(b) and palin(b):
        print(b)
        break
    b+=1