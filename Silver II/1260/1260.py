from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    q = deque()
    visited = [0]*(n+1)
    q.append(v)

    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
        for node in graph[v]:
            if not visited[node]:
                q.append(node)


def dfs(v):
    q = deque()
    visited = [0]*(n+1)
    q.append(v)

    while q:
        v = q.pop()
        if visited[v] == 0:
            visited[v] = 1
            print(v, end=" ")
        for node in sorted(graph[v], reverse=True):
            if not visited[node]:
                q.append(node)


n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

dfs(v)
print()
bfs(v)
