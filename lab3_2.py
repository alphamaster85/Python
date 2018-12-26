import sys

n = int(sys.argv[1])
a = 0
b = 1

if n == 0:
	print (a)
else:
	for counter in range (n-1):
		b = b + a
		a = b - a
	print (b)