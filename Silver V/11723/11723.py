import sys
input = sys.stdin.readline

arr = [0 for i in range(21)]
n = int(input())

for i in range(n):
	cal = input().split()
	if cal[0] == 'add':
		arr[int(cal[1])] = 1
	elif cal[0] == 'remove':
		arr[int(cal[1])] = 0
	elif cal[0] == 'check':
		if arr[int(cal[1])] == 1:
			print(1)
		else:
			print(0)
	elif cal[0] == 'toggle':
		if arr[int(cal[1])] == 1:
			arr[int(cal[1])] = 0
		else:
			arr[int(cal[1])] = 1
	elif cal[0] == 'all':
		arr = [1 for i in range(21)]
	elif cal[0] == 'empty':
		arr = [0 for i in range(21)]