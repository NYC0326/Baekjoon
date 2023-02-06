import sys
input = sys.stdin.readline

n = int(input())
val = []
stk = []
ans = 0
for i in range(n):
    val.append(int(input()))

for i in range(n):
    while stk and val[stk[-1]] > val[i]:
        tmp = stk.pop()
        if stk:
            width = i - stk[-1] - 1
        else:
            width = i
        ans = max(ans, width*val[tmp])
    stk.append(i)

while stk:
    tmp = stk.pop()
    if stk:
        width = n-stk[-1]-1
    else:
        width = n
    ans = max(ans, width*val[tmp])

print(ans)
