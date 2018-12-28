n1 = 2
m1 = 1
n2 = 3
m2 = 5
n3 = 8
m3 = 2
n4 = 9
m4 = 3

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

print(super_fibonacci(n1, m1))
print(super_fibonacci(n2, m2))
print(super_fibonacci(n3, m3))
print(super_fibonacci(n4, m4))