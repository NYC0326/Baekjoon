import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = 1e9


def dijkstra():
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF]*(n)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v, w in graph[now]:
            if edges[now][v]:
                continue
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    return distance


def bfs():
    q = deque()
    q.append(end)

    while q:
        v = q.popleft()
        if v == start:
            continue
        for node, cost in graphReverse[v]:
            if distance[node] + cost == distance[v] and not edges[node][v]:
                edges[node][v] = True
                q.append(node)


while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    start, end = map(int, input().split())
    graph = [[] for _ in range(n)]
    graphReverse = [[] for _ in range(n)]
    edges = [[False]*n for _ in range(n)]
    for i in range(m):
        s, e, v = map(int, input().split())
        graph[s].append((e, v))
        graphReverse[e].append((s, v))
    distance = dijkstra()
    bfs()
    distance = dijkstra()
    if distance[end] == INF:
        print(-1)
    else:
        print(distance[end])
