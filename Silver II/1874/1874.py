import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
c = 1

for i in range(n):
    num = int(input())
    while c <= num:
        stack.append(c)
        ans.append('+')
        c += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        ans = []
        break

if len(ans) != 0:
    for i in ans:
        print(i)
