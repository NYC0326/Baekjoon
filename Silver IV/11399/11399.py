n = int(input())
val = list(map(int, input().split()))
val.sort()
m = 0

for i in range(len(val)):
    m += val[i]*(len(val)-i)

print(m)