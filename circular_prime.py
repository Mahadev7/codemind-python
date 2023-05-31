def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=input()
b=a[::-1]
a1=int(a)
b1=int(b)
if prime(a1) and prime(b1):
    print("circular prime")
if (prime(a1) and not prime(b1)) or (not prime(a1) and prime(b1)):
    print("prime but not a circular prime")
if not prime(a1) and not prime(b1):
    print("not prime")