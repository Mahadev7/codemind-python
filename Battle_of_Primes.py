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
p=0
while True:
    p+=1
    c+=1
    if prime(c):
        break
print(p)