def adddigits(num):
    s=0
    while num>0:
        d=num%10
        num=num//10
        s=s+d
    return s



n=int(input())
while n>9:
    n=adddigits(n)
print(n)