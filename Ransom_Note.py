
def can(r,m):
    r = list(r)
    m = list(m)
    for i in r: # a 
        if i in m: # b
            m.remove(i) # 
        else:
            return False
    return True
r,m = map(str,input().split())
print(can(r,m))