p,q=map(int,input().split())
for i in range(q+1):
    if i%2!=0:
        print(p,"x",i,"=",p*i)