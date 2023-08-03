n, m = map(int, input().split())
memory = [0]+list(map(int, input().split()))
cost = [0]+list(map(int, input().split()))
dp = [[0]*(sum(cost)+1) for _ in range(n+1)]
ans = 10001

for i in range(1, n+1):
    byte, c = memory[i], cost[i]

    for j in range(1, sum(cost)+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-c], dp[i-1][j])

        if dp[i][j] >= m:
            ans = min(ans, j)

print(ans if m else 0)
