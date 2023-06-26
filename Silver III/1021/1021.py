import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
find = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

ans = 0
for i in find:
    cnt = 0
    while True:
        top = q.popleft()
        if top != i:
            cnt += 1
            q.append(top)
        else:
            break
    ans += min(cnt, len(q)+1-cnt)

print(ans)
