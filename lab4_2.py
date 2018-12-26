import sys

str_in = []
for arg in sys.argv[1:]: 
    str_in.append(arg)

str_in.reverse()

str_out = str(str_in[0])
for elem in range(1, len(str_in)):
	str_out = str_out + ' ' + str(str_in[elem])

print (str_out)