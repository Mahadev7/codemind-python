a=input()
x=list(a)
for i in range(len(x)):
    if x[i]=='6':
        x[i]='9'
        break
y="".join(x)
print(y)