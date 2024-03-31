n = int(input())
s = list(input())
val = []
stk = []

for i in range(n):
    val.append(int(input()))

for i in s:
    if i.isalpha():
        stk.append(val[ord(i)-65])
    else:
        b = stk.pop()
        a = stk.pop()

        if i == '+':
            stk.append(a+b)
        elif i == '-':
            stk.append(a-b)
        elif i == '*':
            stk.append(a*b)
        else:
            stk.append(a/b)

print("%.2f" % stk[0])
