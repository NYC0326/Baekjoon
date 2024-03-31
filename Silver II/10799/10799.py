q = input()
stk = []
cnt = 0

for i in range(len(q)):
    if q[i] == '(':
        stk.append(q[i])
    else:
        if q[i-1] == '(':
            stk.pop()
            cnt += len(stk)
        else:
            stk.pop()
            cnt += 1
print(cnt)
