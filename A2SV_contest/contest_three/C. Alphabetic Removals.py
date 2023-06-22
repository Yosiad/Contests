arr=list(map(int, input().split()))
input=input()
for i in range(arr[1]):
    rem=min(input)
    for j in range(len(input)):
        if input[j]==rem:
            input=input[:j]+input[j+1:]
            break
print(input)