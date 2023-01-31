import sys
input = sys.stdin.readline
n, m = map(int, input().split())

pokemon = {}

for i in range(n):
    name = input().strip()
    pokemon[i+1] = name
    pokemon[name] = i+1

for i in range(m):
    find = input().strip()
    if find.isdigit():
        print(pokemon[int(find)])
    else:
        print(pokemon[find])