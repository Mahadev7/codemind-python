def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=input()
b=a[::-1]
a=int(a)
b=int(b)
if prime(a) and prime(b):
    print("circular prime")
elif (prime(a) and not prime(b)) or (prime(b) and not prime(a)):
    print("prime but not a circular prime")
elif not prime(a) and not prime(b):
    print("not prime")