import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a < b+c and b < a+c and c < a+b:
	if a > 0 and b > 0 and c > 0:
		print ('triangle')
	else:
		print ('not triangle')
else:
	print ('not triangle')