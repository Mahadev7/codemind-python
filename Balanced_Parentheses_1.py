def Balanced(n):
    a = '{[('
    b = '}])'
    s = []
    for i in n:
        if i == '{' or i == '[' or i == '(':
            s.append(i)
        else:
            if len(s)==0:
                return False
            if a.index(s[-1])==b.index(i):
                s.pop()
    if len(s)==0:
        return True
    return False
n = input()
print(Balanced(n))