from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
cnt = Counter(arr)
stk = []
ans = [-1] * n

for i in range(n):
    while stk and cnt[arr[stk[-1]]] < cnt[arr[i]]:
        ans[stk.pop()] = arr[i]
    stk.append(i)

print(*ans)
