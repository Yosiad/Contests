n=int(input())
for i in range(n):
    num=int(input())
    arr=list(map(int, input().split()))
    arr=sorted(arr)
    stack=[arr[0]]
    for j in range(1,len(arr)):
        if arr[j]-stack[-1]==1:
            stack.pop()
            stack.append(arr[j])
        elif arr[j]!=stack[-1]:
            stack.append(arr[j])
    if len(stack)==1: print("YES")
    else: print("NO")

