import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password = {}

for i in range(n):
    site, pw = input().split()
    password[site] = pw

for j in range(m):
    find = input().strip()
    print(password[find])