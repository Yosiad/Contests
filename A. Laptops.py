n=int(input())
price=list(map(int, input().split()))
quality=list(map(int, input().split()))
pr_qu=[]
for i in range(n):
    pr_qu+=[(price[i],quality[i])]
vals=[]
for j in pr_qu:
    vals.append(j[1])
if vals==sorted(vals)[::-1]:
    print('Happy Alex')
else:
    print('Poor Alex')
