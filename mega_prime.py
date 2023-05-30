def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
if isprime(a):
    while a:
        d=a%10
        a=a//10
        if not isprime(d):
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")