import sys
input = sys.stdin.readline

n = int(input())
val = [0]*1001
max_w = 0
max_h = 0
end_w = 0
for i in range(n):
    w, h = map(int, input().split())
    val[w] = h
    if h > max_h:
        max_h = h
        max_w = w
    if w > end_w:
        end_w = w

h = 0
ans = 0
for i in range(max_w+1):
    if h < val[i]:
        h = val[i]
    ans += h

h = 0
for i in reversed(range(max_w+1, end_w+1)):
    if h < val[i]:
        h = val[i]
    ans += h

print(ans)
