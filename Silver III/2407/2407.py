n, m = map(int, input().split())
cnt = 1;

for i in reversed(range(n-m+1, n+1)):
    cnt *= i

for i in range(1, m+1):
    cnt //= i

print(cnt)