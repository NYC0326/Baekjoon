import sys
input = sys.stdin.readline
T = int(input())

chk = [1] * 1000001
chk[0], chk[1] = 0, 0
prime = []

for i in range(2, 1000001):
    if chk[i]:
        prime.append(i)
    for j in range(2*i, 1000001, i):
        chk[j] = 0

for _ in range(T):
    N = int(input())
    cnt = 0
    for i in prime:
        if i >= N:
            break
        if chk[N-i] and i <= N-i:
            cnt += 1
    print(cnt)