import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not graph[nx][ny][nz]:
                q.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z]+1


m, n, h = map(int, input().split())
graph = []
q = deque()
ans = 0

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append((i, j, k))
    graph.append(tmp)

bfs()
for i in graph:
    for j in i:
        for k in j:
            if not k:
                print(-1)
                exit()
        ans = max(ans, max(j))
print(ans-1)
