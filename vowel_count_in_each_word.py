a=input()
a=a.split()
x='aeiou'
for i in a:
    c=0
    i.lower()
    for j in i:
        if j in x:
            c+=1
    print(c,end=' ')