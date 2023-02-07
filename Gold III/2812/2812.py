n, k = map(int, input().split())
num = input()
stk = []

for i in num:
    while stk and stk[-1] < i and k > 0:
        stk.pop()
        k -= 1
    stk.append(i)

if k > 0:
    print(''.join(stk[:-k]))
else:
    print(''.join(stk))
