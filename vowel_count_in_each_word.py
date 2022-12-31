a=input()
c=0
for j in a:
    if j=='a':
        c+=1
    if j=='e':
        c+=1
    if j=='i':
        c+=1
    if j=='o':
        c+=1
    if j=='u':
        c+=1
    if j==' ':
        print(c,end=' ')
        c=0
print(c)