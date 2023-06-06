def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
    
n=input()
l=list(n)
s=0
for i in l:
    i=int(i)
    s+=fact(i)
if s==int(n):
    print(f"The number {n} is a strong number")
else:
    print(f"The number {n} is not a strong number")