a=input()
b=a.split()
v='aeiou'
l=[]
for i in b:
    c=0
    i=i.lower()
    for j in i:
        if j in v:
            c+=1
    l.append(c)
x=min(l)
print(l.count(x))