import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stk = []
ans = [0] * n

for i in range(len(arr)):
    while stk and arr[stk[-1]] < arr[i]:
        stk.pop()
    if stk:
        ans[i] = stk[-1] + 1
    stk.append(i)

print(*ans)
