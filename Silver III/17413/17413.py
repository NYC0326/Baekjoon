s = input()
ans = []
stk = []
bracket = False


def flip():
    global ans, stk
    while stk:
        ans.append(stk[-1])
        stk.pop()


for i in s:
    if i == '<':
        flip()
        bracket = True
    elif i == '>':
        bracket = False
    if i == ' ':
        flip()
    if bracket == True or i == ' ' or i == '>':
        ans.append(i)
    else:
        stk.append(i)
    # print(ans, stk)

flip()
print(''.join(ans))
