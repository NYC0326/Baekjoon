import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    k = int(input())
    dict = {}
    for j in range(k):
        gear, part = input().split()
        if part in dict:
            dict[part] += 1
        else:
            dict[part] = 1
    ans = 1
    for j in dict.keys():
        ans *= dict[j]+1
    print(ans-1)    