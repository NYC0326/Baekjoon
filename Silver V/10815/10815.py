import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
chk = list(map(int, input().split()))
ans = [0] * 20000001

for i in arr:
    ans[i+10000000] = 1

for i in chk:
    print((ans[i+10000000]), end=" ")