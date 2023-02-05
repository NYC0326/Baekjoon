while True:
    s = input()
    stack = []
    check = True
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                check = False
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                check = False
                break
            else:
                stack.pop()
    if check == True and not stack:
        print('yes')
    else:
        print('no')
