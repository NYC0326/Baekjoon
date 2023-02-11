import sys
from collections import deque
input = sys.stdin.readline

num = int(input())


def bfs(graph, n, m):
    ans = 0
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if graph[j][i] == 1:
                q.append((i, j))
                graph[j][i] = 0
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]

                        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 1:
                            q.append((nx, ny))
                            graph[ny][nx] = 0
                ans += 1

    return ans


for _ in range(num):
    n, m, cnt = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for _ in range(cnt):
        x, y = map(int, input().split())
        graph[y][x] = 1
    print(bfs(graph, n, m))
