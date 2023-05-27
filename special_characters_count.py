a=input()
l=[]
u =0 
for i in a:
    if i.isalpha() or i.isnumeric() or i==' ':
        continue
    u+=1
print(u)