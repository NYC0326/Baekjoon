import sys
input = sys.stdin.readline

n = int(input())
stk = []
max = 0
ans = 0
for i in range(n):
    stk.append(int(input()))

while stk:
    tmp = stk.pop()
    if tmp > max:
        max = tmp
        ans += 1

print(ans)
