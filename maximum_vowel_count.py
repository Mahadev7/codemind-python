a=input()
a=a.split()
v='aeiou'
c=0
p=[]
for i in a:
    c=0
    i.lower()
    for j in i:
        if j in v:
            c+=1
        p.append(c)
print(max(p))