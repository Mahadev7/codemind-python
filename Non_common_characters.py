a=input()
b=input()
a=a.lower()
b=b.lower()
a1,b1=[],[]
c=0
for i in a:
    if i.isalpha():
        a1.append(i)
for i in b:
    if i.isalpha():
        b1.append(i)
l=set(a1)
m=set(b1)
for i in l:
    if i not in m:
        c+=1
for i in m:
    if i not in l:
        c+=1
print(c)