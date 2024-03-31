import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for i in range(n):
    word = input().rstrip()
    if word not in dict.keys() and len(word) >= m:
        dict[word] = [1, len(word), word]
    elif word in dict.keys():
        dict[word][0] += 1

values = list(dict.values())

values.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in values:
    print(i[2])
