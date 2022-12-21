def palin(m):
    p=0
    r=0
    while m:
        p=m%10
        r=(r*10)+p
        m=m//10
    return r
n=int(input())
for i in range(n):
    b=int(input())
    if palin(b)==b:
        print("True")
    else:
        print("False")
