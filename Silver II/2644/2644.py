import sys
input = sys.stdin.readline

def dfs(v):
    for n in graph[v]:
        if not visited[n]:
            visited[n] = visited[v]+1
            dfs(n)

n = int(input())                    # 전체 사람 수
a, b = map(int, input().split())    # 촌수 계산해야하는 두 사람
m = int(input())                    # 부모 자식 관계 수
graph = [[] for _ in range(n+1)]    # 부모 자식 관계 저장할 그래프
visited = [0]*(n+1)                 # 방문 목록 저장

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(a)
print(visited[b] if visited[b]>0 else -1)