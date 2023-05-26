a=input()
b='AEIOUaeiou'
c=[]
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(*c)