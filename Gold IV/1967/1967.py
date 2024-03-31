import sys
from collections import deque
input = sys.stdin.readline


def dfs(v):
    dis = [-1]*(n+1)
    q = deque()
    q.append(v)
    dis[v] = 0
    maxInfo = [0, 0]

    while q:
        v = q.pop()
        for e, w in graph[v]:
            if dis[e] == -1:
                dis[e] = dis[v]+w
                q.append(e)
                if maxInfo[0] < dis[e]:
                    maxInfo = dis[e], e

    return maxInfo


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

ans, node = dfs(1)
ans, node = dfs(node)
print(ans)
