list1 = [1, 1.0, '1', -1, 1]
list2 = ['qwe', 'reg', 'qwe', 'REG']
list3 = [32, 32.1, 32.0, -123]
list4 = [1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]

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

print(clean_list(list1))
print(clean_list(list2))
print(clean_list(list3))
print(clean_list(list4))