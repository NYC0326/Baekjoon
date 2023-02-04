n = int(input())

for i in range(n):
    cal = input().split()
    cal[0] = int(cal[0])
    for j in range(1, len(cal)):
        if cal[j] == "@":
            cal[0] *= 3
        elif cal[j] == "%":
            cal[0] += 5
        elif cal[j] == "#":
            cal[0] -= 7
	print("%.2f" % )