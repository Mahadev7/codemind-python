def pal(n):
    r=0
    while n:
        a=n%10
        r=r*10+a
        n=n//10
    return r
n=int(input()) # 95
while n:
    a=pal(n)
    b=a+n # 95+59
    if pal(b)==b:# 59==154
        print(b)
        break
    n=b # 154