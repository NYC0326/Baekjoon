import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 우선순위 큐, 시작 정점의 거리는 0으로 설정
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:  # 이미 방문한 노드이면 패스
            continue

        for i in graph[now]:  # 연결된 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 현재 노드를 거쳐서 가는 것이 더 짧다면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m = map(int, input().split())
k = int(input())
INF = 1e9  # 10억, 무한
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, n+1):
    print("INF" if distance[i] == INF else distance[i])
