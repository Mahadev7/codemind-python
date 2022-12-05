a=int(input())
for i in range(a+1):
    p,q,r,s=map(int,input().split())
    Fran=p/q
    Ven=p/r
    t=p/(q*r)
    if Fran>=s or Ven>=s or t>=s:
        print("Win")
    else:
        print("Lose")