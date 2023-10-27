n = input()
p=''
r,res = [],[]
for i in range(len(n)):
    if n[i] in 'aeiou':
        p+='V'
    else:
        p+='C'
p = list(p)
for i in range(len(p)-1):
    if p[i]==p[i+1]:
        r.append(i)
for i in range(len(p)):
    if i not in r:
        res.append(p[i])
print(''.join(res))