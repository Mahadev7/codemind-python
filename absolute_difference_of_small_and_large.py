a=input()
b=a.split()
c=[]
for i in b:
    x=min(i)
    y=max(i)
    m=ord(x)
    n=ord(y)
    print(abs(m-n),end=' ')