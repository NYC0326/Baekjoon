arr = [0, 1, 2]
n = int(input())

if n<3:
    print(arr[n])

else:
    for i in range(n-2):
        arr.append((arr[i+1]+arr[i+2])%10007)
    print(arr[n])