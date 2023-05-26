a=input()
m=[]
for i in a:
    if i.isalpha():
        m.append(i)
b=min(m)
c=max(m)
d=m.count(b)
e=m.count(c)
print(b,d,c,e)