import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, h):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


n = int(input())
maxNum = 0
graph = []
result = []

for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

    for j in tmp:
        if j > maxNum:
            maxNum = j

for i in range(maxNum):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[j][k]:
                bfs(j, k, i)
                cnt += 1
    result.append(cnt)

print(max(result))
