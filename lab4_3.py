import sys

string = sys.argv[1]
flag = False
counter = 0
is_true = True

for elem in range(len(string)):
	if string[elem] == ")" and counter < 1:
		is_true = False
		break
	if string[elem] == "(":
		counter = counter + 1
	elif string[elem] == ")":
		counter = counter - 1

if counter == 0:
	flag = True

if is_true == True:
	if flag == True:
		print ('YES')
	else:
		print ('NO')
else:
	print ('NO')