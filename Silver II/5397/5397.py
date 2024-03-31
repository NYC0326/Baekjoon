import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    s = input().rstrip()
    stk_1 = []
    stk_2 = []
    for j in s:
        if j == '<' and stk_1:
            stk_2.append(stk_1.pop())
        elif j == '>' and stk_2:
            stk_1.append(stk_2.pop())
        elif j == '-' and stk_1:
            stk_1.pop()
        elif j not in ['<', '>', '-']:
            stk_1.append(j)
    print(''.join(stk_1+list(reversed(stk_2))))
