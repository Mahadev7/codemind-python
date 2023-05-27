a=input()
b=a.split()
v='aeiou'
c=0
l=[]
for i in b:
    c=0
    i.lower()
    for j in i:
        if j in v:
            c+=1
        l.append(c)
print(max(l))