a=input()
a=a.lower()
b=[]
for i in a:
    if i.isalpha():
        b.append(i)
print(max(b))