n, m = map(int, input().split())
a = [0]*(n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    a[i:j+1] = [k]*(j-i+1)

print(' '.join(list(map(str, a[1:]))))
