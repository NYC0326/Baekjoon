import sys
import heapq
input = sys.stdin.readline
INF = 1e9


def dijkstra(start, end):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

    return distance[end]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

s1, s2 = map(int, input().split())

ans1 = dijkstra(1, s1) + dijkstra(s1, s2) + dijkstra(s2, n)
ans2 = dijkstra(1, s2) + dijkstra(s2, s1) + dijkstra(s1, n)

if ans1 >= INF and ans2 >= INF:
    print(-1)
else:
    print(min(ans1, ans2))
