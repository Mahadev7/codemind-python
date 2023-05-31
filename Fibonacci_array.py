def fibanocci(z): #
    a=z[0] # 1 
    b=z[1] # 2
    for i in range(2,len(z)):
        if z[i]==a+b: # 1 2
            a=b # 2 2 
            b=z[i] # 3
        else:
            return False
    return True
n=int(input())
x=list(map(int,input().split())) # 1 2 3 5 8 9 13
if len(x)<=2:
    print('no')
elif fibanocci(x):
    print("yes")
else:
    print("no")