n, m = map(int, input().split())
cnt = 1

while m != n:
    if m < n:
        cnt = -1
        break
    if m % 10 == 1:
        m //= 10
    elif m % 2 == 0:
        m //= 2
    else:
        cnt = -1
        break
    cnt += 1

print(cnt)
