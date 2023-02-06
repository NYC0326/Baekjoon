n = int(input())
cnt = 0

for i in range(n):
    s = input()
    stk = []
    for a in s:
        if stk and stk[-1] == a:
            stk.pop()
        else:
            stk.append(a)
    if not stk:
        cnt += 1
print(cnt)
