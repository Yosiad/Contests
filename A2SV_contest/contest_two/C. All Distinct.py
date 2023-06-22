n=int(input())
for i in range(n):
    num=int(input())
    arr=list(map(int, input().split()))
    if sorted(arr)==arr or sorted(arr)[::-1]==arr:
        print("YES")
    else:
        for j in range(2,len(arr)-1):
            if sorted(arr[:j])+sorted(arr[j:])[::-1]==arr:
                print("YES")
                break
        else: print("NO")