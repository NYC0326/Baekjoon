string = input().strip()
find = input().strip()
stack = []

for c in string:
    stack.append(c)
    if c == find[-1] and ''.join(stack[-len(find):]) == find:
        del stack[-len(find):]

ans = ''.join(stack)

if ans == '':
    print("FRULA")
else:
    print(ans)