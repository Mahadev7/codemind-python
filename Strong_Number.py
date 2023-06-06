def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
a=input()
s=0
l=list(a)
for i in l:
    i=int(i)
    s+=fact(i)
if s==int(a):
    print(f"The number {a} is a strong number")
else:
    print(f"The number {a} is not a strong number")

