import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
stk = []

for i in range(n):
    while stk and arr[stk[-1]] < arr[i]:
        ans[stk.pop()] = arr[i]
    stk.append(i)

print(*ans)
