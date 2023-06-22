n=int(input())
arr=list(map(int, input().split()))
positive = 0
negative = 0
zero = 0

ans = 0
for i in range(n):
    if (arr[i] == 0):
        zero += 1
    elif (arr[i] < 0):
        negative += 1
        ans = ans + (-1 - arr[i])
    else:
        positive += 1

        ans = ans + (arr[i] - 1)
if (negative % 2 == 0):
    ans = ans + zero

else:

    if (zero > 0):

        ans = ans + zero
    else:
        ans = ans + 2
print(ans)