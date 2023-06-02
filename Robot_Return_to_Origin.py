a=input()
x=0
y=0
for i in a:
    if i=='U':
        x+=1
    if i=='D':
        x-=1
    if i=='L':
        y+=1
    if i=='R':
        y-=1
if x==0 and y==0:
    print("True")
else:
    print("False")