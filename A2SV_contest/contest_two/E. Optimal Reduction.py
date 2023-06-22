n=int(input())
for i in range(n):
    num=int(input())
    arr=list(map(int, input().split()))
    if len(set(arr))==len(arr):
        print("YES")
    else: print("NO")