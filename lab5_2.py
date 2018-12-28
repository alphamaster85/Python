a1 = 12345
b1 = 567
a2 = 1233211
b2 = 12128
a3 = 123
b3 = 45

def counter(a, b):
	a = str(a)
	b = str(b)
	count = 0
	list_a = []
	list_b = []

	def clean_list(list1):
		if list1 == []:
			return (list1)

		list2 = []
		list2.append(list1[0])

		for i in range(1, len(list1)):
			flag = False
			for j in range(i):
				if list1[i] is list1[j]:
					flag = True

			if flag == False:
				list2.append(list1[i])

		if list2 == []:
			return (list1)
		return (list2)
	
	for e in a:
		list_a.append(e)

	for e in b:
		list_b.append(e)

	list_b = clean_list(list_b)

	for i in range(len(list_b)):
		for j in range(len(list_a)):
			if list_b[i] is list_a[j]:
				count = count + 1
				break
	return count

print (counter(a1, b1))
print (counter(a2, b2))
print (counter(a3, b3))