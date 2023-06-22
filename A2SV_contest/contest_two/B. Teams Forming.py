n=int(input())
arr=list(map(int, input().split()))
arr=sorted(arr)
ans=0
for i in range(1,len(arr),2):
    ans+=arr[i]-arr[i-1]
print(ans)