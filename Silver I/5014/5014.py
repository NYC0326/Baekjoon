import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [0]*(f+1)
cnt = [0]*(f+1)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == g:
            return cnt[v]
        for i in (v+u, v-d):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                cnt[i] = cnt[v]+1
                q.append(i)
    return 'use the stairs'


print(bfs(s))
