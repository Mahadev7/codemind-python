a=int(input())
x=0
y=1
while y<a:
    z=x+y
    x=y
    y=z
if abs(x-a)<abs(y-a):
    print(x)
elif abs(x-a)==abs(y-a):
    print(x,y)
else:
    print(y)