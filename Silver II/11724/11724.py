import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
ans = 0


def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for n in graph[v]:
            if not visited[n]:
                q.append(n)
                visited[n] = 1


for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            ans += 1
            visited[i] = 1
        else:
            bfs(i)
            ans += 1

print(ans)
