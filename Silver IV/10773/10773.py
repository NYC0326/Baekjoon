import sys
from collections import deque
input = sys.stdin.readline

stk = deque()
k = int(input())
sum = 0
for _ in range(k):
    n = int(input())
    if n:
        stk.append(n)
        sum += n
    else:
        p = stk.pop()
        sum -= p

print(sum)