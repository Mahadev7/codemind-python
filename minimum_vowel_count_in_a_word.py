a=input()
a=a.split()
v='aeiou'
l=[]
for i in a:
    c=0
    i = i.lower()
    for j in i:
        if j in v:
            c+=1
    l.append(c)
print(min(l))