n1 = '123'
n2 = 906
n3 = '001'
n4 = -8
n5 = -8.0

def count_holes(n):
	if isinstance(n, float):
		return '1'
	elif isinstance(n, str):
		return 's'		
	else:
		return 'ERROR'

print(count_holes(n1))
print(count_holes(n2))
print(count_holes(n3))
print(count_holes(n4))
print(count_holes(n4))