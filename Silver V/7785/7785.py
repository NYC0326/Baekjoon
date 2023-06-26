import sys
input = sys.stdin.readline

n = int(input())

office = {}

for _ in range(n):
    name, check = map(str, input().split())
    if check == 'enter':
        office[name] = True
    else:
        del office[name]

names = sorted(office, reverse=True)

for name in names:
    print(name)
