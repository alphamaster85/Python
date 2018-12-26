import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
counter = 0
sum1 = 0
sum2 = 0
digit = ''

for n in range(a1, a2+1):
	if n < 10:
		digit = '00000' + str(n)
	elif n < 100 and n >= 10:
		digit = '0000' + str(n)
	elif n < 1000 and n >= 100:
		digit = '000' + str(n)
	elif n < 10000 and n >= 1000:
		digit = '00' + str(n)
	elif n < 100000 and n >= 10000:
		digit = '0' + str(n)
	else:
		digit = str(n)
	
	for elem in range(3):
		sum1 = sum1 + int(digit[elem])
	for elem in range(3, 6):
		sum2 = sum2 + int(digit[elem])
	
	if sum1 == sum2:
		counter = counter + 1
		
	sum1 = 0
	sum2 = 0

print (counter)