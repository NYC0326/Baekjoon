a = [list(map(int, input().split())) for _ in range(9)]

max=0
max_index =[0,0]
for i in range(9):
    for j in range(9):
        if a[i][j]>=max:
            max=a[i][j]
            max_index=[i+1,j+1]

print(max)
print(max_index[0],max_index[1])