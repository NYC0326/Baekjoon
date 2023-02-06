import sys
input = sys.stdin.readline

while True:
    stk = []
    ans = 0
    val = list(map(int, input().split()))
    n = val.pop(0)
    if n == 0:
        break

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
