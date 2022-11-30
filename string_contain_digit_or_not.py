a=input()
x=[]
for i in a:
    if i.isdigit():
        x.append(i)
l=len(x)
if l==0:
    print("Doesn't contain digit")
else:
    print("Contains %d digit"%l)