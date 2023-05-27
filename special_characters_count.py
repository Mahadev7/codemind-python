a=input()
x=[]
y=[]
for i in a:
    if i.isalpha() or i.isnumeric() or i==' ':
        x.append(i)
    else:
        y.append(i)
print(len(y))