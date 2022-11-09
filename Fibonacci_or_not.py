n=int(input())
a=0
b=1
for i in range(2,n):#(2,10)(a,b)
    c=a+b
    if c==n:
        print("True")
        break
    a=b #1
    b=c #1
if c>n: #1>10
    print("False")
    
