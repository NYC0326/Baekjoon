import sys
import heapq
input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

s, e = map(int, input().split())
dijkstra(s)
print(distance[e])
