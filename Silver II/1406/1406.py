import sys
input = sys.stdin.readline

stk = list(input().strip())
stk2 = []
n = int(input())

for i in range(n):
    cmd = input().split()
    if cmd[0] == 'L' and stk:
        stk2.append(stk.pop())
    elif cmd[0] == 'D' and stk2:
        stk.append(stk2.pop())
    elif cmd[0] == 'B' and stk:
        stk.pop()
    elif cmd[0] == 'P':
        stk.append(cmd[-1])

print(''.join(stk+list(reversed(stk2))))
