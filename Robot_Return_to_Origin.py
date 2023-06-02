a=input()
x=0
y=0
l=[]
for i in a:
    if i.isalpha() and(i=='U' or i=='D' or i=='L' or i=='R'):
        l.append(i)
for i in l:
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