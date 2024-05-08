from collections import deque

n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
ans = []
cnt = 1
while arr:
    if cnt==k:
        ans.append(arr.popleft())
        cnt = 1
    else:
        cnt+=1
        arr.append(arr.popleft())

print("<", end="")
print(", ".join(list(map(str, ans))), end="")
print(">", end="")