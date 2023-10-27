n = input()
m,c = 0,0
v = 'aeiou'
for  i in n:
    if i in v:
        c+=1
        m = max(m,c)
    else:
        c = 0
print(m)