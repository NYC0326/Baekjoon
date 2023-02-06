str = input()
stk = []
ans = 0
cnt = 1

for i in range(len(str)):
    if str[i] == '(':
        stk.append(str[i])
        cnt *= 2
    elif str[i] == ')':
        if str[i-1] == '(':
            ans += cnt
        if not stk or stk[-1] == '[':
            ans = 0
            break
        stk.pop()
        cnt //= 2
    elif str[i] == '[':
        stk.append(str[i])
        cnt *= 3
    else:
        if str[i-1] == '[':
            ans += cnt
        if not stk or stk[-1] == '(':
            ans = 0
            break
        stk.pop()
        cnt //= 3

if stk:
    ans = 0
print(ans)
