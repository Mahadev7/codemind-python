x=int(input())
p=0
q=1
r=0
while x:
    print(p,end=' ')
    r=p+q
    p=q
    q=r
    # r+=1
    x-=1