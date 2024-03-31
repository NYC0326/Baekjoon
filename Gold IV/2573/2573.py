import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    melt = []

    while q:
        x, y = q.popleft()
        sea = 0
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:  # 주변이 바다라면
                    sea += 1    # 바다 개수 업데이트
                elif graph[nx][ny] and not visited[nx][ny]:  # 아직 방문하지 않은 빙하라면
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea:
            melt.append((x, y, sea))

    for x, y, sea in melt:
        graph[x][y] = max(0, graph[x][y]-sea)

    return 1  # 한번 탐색을 하면, 1개의 빙하 그룹이 탐색 됐을 것이므로 그룹 개수 반환


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ice = []
year = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

while ice:
    visited = [[0]*m for _ in range(n)]
    melted = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if not graph[i][j]:  # 녹았으면
            melted.append((i, j))
    if group > 1:  # 1개 이상의 그룹으로 나눠지면
        print(year)
        break  # 종료

    ice = sorted(list(set(ice)-set(melted)))
    year += 1

if group < 2:
    print(0)
