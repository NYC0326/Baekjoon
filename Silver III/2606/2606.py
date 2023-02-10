import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)


def bfs(v):
    q = deque()
    q.append(v)
    cnt = 0
    visited = [0] * (n+1)

    while q:
        v = q.popleft()
        if visited[v] == 0:
            visited[v] = 1
            cnt += 1
        for node in graph[v]:
            if visited[node] == 0:
                q.append(node)

    return cnt-1


print(bfs(1))
