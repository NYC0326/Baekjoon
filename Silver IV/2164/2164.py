from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])
cnt = 0

while len(q) != 1:
    if cnt % 2 == 0:
        q.popleft()
    else:
        top = q.popleft()
        q.append(top)
    cnt += 1

print(q[0])
