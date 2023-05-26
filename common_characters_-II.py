a=input()
b=input()
a=a.lower()
b=b.lower()
c=0
a1,b1=[],[]
for i in a:
    if i.isalpha():
        a1.append(i)
for i in b:
    if i.isalpha():
        b1.append(i)
a2=set(a1)
b2=set(b1)
for i in a2:
    if i in b2:
        c+=1
print(c)