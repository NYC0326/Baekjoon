from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    a, b = input().split()
    q.append((a, b))

while True:
    if len(q) == 1:
        print(q[0][0])
        break
    name, num = q.popleft()
    for i in range((int(num)-1) % len(q)):
        a, b = q.popleft()
        q.append((a, b))
    q.popleft()
