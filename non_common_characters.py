a=input()
b=input()
a=a.lower()
b=b.lower()
l,m=[],[]
for i in a:
    if i.isalpha():
        l.append(i)
for i in b:
    if i.isalpha():
        m.append(i)
p=set(l)
q=set(m)
z=[]
for i in p:
    if i not in q:
        z.append(i)
for i in q:
    if i not in p:
        z.append(i)
res=sorted(z)
c="".join(res)
print(c)