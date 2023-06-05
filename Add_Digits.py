def add(n):
    s=0
    while n:
        p=n%10
        s+=p
        n=n//10
    return s
x=int(input())
while x>9:
    x=add(x)
print(x)