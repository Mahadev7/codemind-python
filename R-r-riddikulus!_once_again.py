# 5 1 2 3 4
# 5 4
n,k = map(int,input().split())
x = list(map(int,input().split()))
p = x[:k]
q = x[k:]
print(*(q+p))