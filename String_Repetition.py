
n=input()
t = int(input())
x = t//len(n)
y = t%len(n)
# print(x,y)
p=(n.count('a'))* x
# print(c1)
z= n[:y]
q= z.count('a') 
print(p+q)