def pal(n):
    r=0
    while n:
        a=n%10
        r=r*10+a
        n=n//10
    return r # 64521
n,k=map(int,input().split()) # 21546 2
n1=pal(n) # pal(21546)
a=n%(10**k) # 
b=n1%(10**k)#12 
c=pal(b)# palin(12)=21
print(abs(a-c)) # 