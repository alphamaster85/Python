n1 = '123'
n2 = 906
n3 = '001'
n4 = -8
n5 = -8.0
n6 = [1]
n7 = None
n8 = 'qq'
n9 = 888888888888888888888
n10 = -888888888888888888888
n11 = '888888888888888888888'

def count_holes(n):
	if isinstance(n, float) or isinstance(n, list) or n == None:
		return 'ERROR'
	elif isinstance(n, str) and (n[0] != '0' and n[0] != '1' and n[0] != '2' and n[0] != '3' and n[0] != '4' and n[0] != '5' and n[0] != '6' and n[0] != '7' and n[0] != '8' and n[0] != '9'):
		return 'ERROR'
	elif isinstance (int(n), int):
		n = str(int(n))
		counter = 0
		for l in n:
			if l == '0' or l == '4' or l == '6' or l == '9':
				counter = counter + 1
			elif l == '8':
				counter = counter + 2
		return counter
	else:
		return 'ERROR'

print(str(n1) + '	n1 : ' + str(count_holes(n1)))
print(str(n2) + '	n2 : ' + str(count_holes(n2)))
print(str(n3) + '	n3 : ' + str(count_holes(n3)))
print(str(n4) + '	n4 : ' + str(count_holes(n4)))
print(str(n5) + '	n5 : ' + str(count_holes(n5)))
print(str(n6) + '	n6 : ' + str(count_holes(n6)))
print(str(n7) + '	n7 : ' + str(count_holes(n7)))
print(str(n8) + '	n8 : ' + str(count_holes(n8)))
print(str(n9) + '	n9 : ' + str(count_holes(n9)))
print(str(n10) + '	n10 : ' + str(count_holes(n10)))
print(str(n11) + '	n11 : ' + str(count_holes(n11)))