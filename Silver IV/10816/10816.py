import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 20000001
for i in arr:
    cnt[i] += 1

M = int(input())
q = list(map(int, input().split()))

for i in q:
    print(cnt[i], end=" ")