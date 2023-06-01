a=input()
b=list(a)
for i in range(len(b)):
    if b[i]=='6':
        b[i]='9'
        break
p="".join(b)
print(p)