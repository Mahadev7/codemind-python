def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=a+b
s=0
while True:
    s+=1
    c+=1
    if prime(c):
        break
print(s)