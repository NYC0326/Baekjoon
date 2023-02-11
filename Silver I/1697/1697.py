import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]*100001


def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m:
            return arr[x]
        nxt = [x-1, x+1, 2*x]
        for next in nxt:
            if 0 <= next < 100001 and not arr[next]:
                arr[next] = arr[x]+1
                q.append(next)


print(bfs(n))
