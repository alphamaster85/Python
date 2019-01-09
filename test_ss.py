print(1/2)

name1 = ['Amir', 'ccc']
if 'amir' in name1:
	print (1)
else:
	print (2)

x = 4.5
y = 2
print (x//y)

one = chr(104)
two = chr(105)
print(one + two)

con = {}
con[1] = 1
con['1'] = 2
con[1.0] = 4

sum = 0
for k in con:
	sum += con[k]
print(sum)

mt = (1, 2, 3, 4)
# mt.append((5, 6, 7))
print(len(mt))

def m_f(x, y, z, a):
	print(x + y)
nums = [1, 2, 3, 4]
m_f(*nums)

class Person:
	def __init__(self, id):
		self.id = id
obama = Person(100)
obama.__dict__['age'] = 49
print(obama.age + len(obama.__dict__))

import math
print(math.floor(5.5))
print (0xA + 0xa)
print("\x48\x49")

nums = set([1,1,2,3,3,3,4])
print(len(nums))

a = [1,2,3,None,(),[],]
print(len(a))

def addIthem(listParam):
	listParam += [1]
myList = [1, 2, 3, 4]
addIthem(myList)
print(len(myList))

d = lambda p: p*2
t = lambda p: p*3
x =2
x = d(x)
x = t(x)
x = d(x)
print(x)

print(type(1J))

def fibo_element(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		first = 1
		second = 1
		tmp = 0
		for i in range(3, n+1):
			tmp = second
			second = second + first
			first =  tmp
		return second
print('fibo = ' + str(fibo_element(9)))

def count_symbols (word):
	if isinstance(word, str):
		dict = {}
		for l in range(len(word)):
			dict[word[l]] = l + 1
		return dict
	else:
		return False
print(count_symbols('word'))

class parent:
	def __init__(self, param):
		self.v1 = param
class child(parent):
	def __init__(self, param):
		self.v2 = param
obj = child(11)
# print(obj.v1 + ' ' + obj.v2)