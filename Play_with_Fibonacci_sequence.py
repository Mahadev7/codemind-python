n=int(input())
a=0
b=1
c=0
while n:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    c+=1
    n-=1