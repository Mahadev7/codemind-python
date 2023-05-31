def fun(n):
    a=n[0]
    b=n[1]
    for i in range(2,len(n)):
        if n[i]==a+b:
            a=b
            b=n[i]
        else:
            return False
    return True
n=int(input())
x=list(map(int,input().split()))
if len(x)<=2:
    print('no')
elif fun(x):
    print("yes")
else:
    print("no")
        