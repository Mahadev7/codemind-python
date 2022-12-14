def palin(n):
    rev=0
    p=0
    while (n>0):
        p=n%10
        rev=(rev*10)+p
        n=n//10
    return rev
a=int(input())
b=int(input())
for i in range(a,b):
    if i==palin(i):
        print(i,end=" ")