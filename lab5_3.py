n = 9
m = 3

def super_fibonacci(n, m):
	list = []

	for i in range(m):
		list.append(1)
		
		if i == n:
			return list[i]

	for i in range(m, n):
		elem = 0
		for j in range(i-m, i):
			elem = elem + list[j]
		list.append(elem)

		if i == n-1:
			return list[i]

print(super_fibonacci(n, m))