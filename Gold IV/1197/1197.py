import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
visited = [0] * (V+1)
graph = [[] for _ in range(V+1)]
heap = [(0, 1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

ans = 0
cnt = 0

while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = 1
        ans += w
        cnt += 1
        for i in graph[s]:
            heapq.heappush(heap, i)

print(ans)
