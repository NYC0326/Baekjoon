import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())
for i in range(n):
    a = input().split()
    if len(a) == 2:
        q.append(int(a[1]))
    else:
        if a[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                p = q.popleft()
                print(p)
        if a[0] == 'size':
            print(len(q))
        if a[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        if a[0] == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        if a[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])