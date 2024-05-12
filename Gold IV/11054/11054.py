N = int(input())
arr = list(map(int, input().split()))
reversed_arr = arr[::-1]
increase = [1] * N
decrease = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reversed_arr[i] > reversed_arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

ans = [increase[i] + decrease[i] for i in range(N)]
print(max(ans))