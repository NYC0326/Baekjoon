import sys
input = sys.stdin.readline

n, val = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)
cnt = 0

for i in range(len(coin)):
    cnt += val//coin[i]
    val %= coin[i]

print(cnt)