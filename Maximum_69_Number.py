a=input()
p=list(a)
for i in range(len(p)):
    if p[i]=='6':
        p[i]='9'
        break
x="".join(p)
print(int(x))