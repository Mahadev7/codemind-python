def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
x=int(input())
y=int(input())
z=x+y
p=0
while True:
    p+=1
    z=z+1
    if prime(z):
        break
print(p)