import sys

string = sys.argv[1]
srting_modifity = string.replace(" ", '').lower()
str_list = []

for letter in srting_modifity:
	str_list.append(letter)

str_reverse = str_list
str_reverse.reverse()

flag = True
for elem in range(len(str_reverse)):
	if srting_modifity[elem] != str_reverse[elem]:
		flag = False
if flag == True:
	print ('YES')
else:
	print ('NO')