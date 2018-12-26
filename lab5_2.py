a = 1233211
b = 12128

def counter(a, b):
	a = str(a)
	b = str(b)

	count = 0

	list_a = []
	list_b = []

	for e in a:
		list_a.append(e)

	for e in b:
		list_b.append(e)

	for i in range(len(list_b)):
		for j in range(len(list_a)):
			if list_b[i] is list_a[j]:
				count = count + 1
				break
	return count

print (counter(a, b))