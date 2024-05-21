K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))
ans = 0

def search(low, high):
    global ans, N
    if low > high:
        return
    mid = (low+high)//2
    cnt = 0
    for i in lan:
        cnt += i//mid
    if cnt >= N:
        ans = mid
        search(mid+1, high)
    else:
        search(low, mid-1)

search(0, max(lan)*2)
print(ans)