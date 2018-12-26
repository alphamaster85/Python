import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

text_code = sys.argv[1]
text_code = text_code.replace(" ", '')
text_code = text_code[:(len(text_code)-(len(text_code)%5))]

list_uncode = []
for letter in text_code:
	if letter < 'a':
		list_uncode.append('b')
	else:
		list_uncode.append('a')

list_key = []
for letter in key:
	list_key.append(letter)

text_small = ''
text_uncode = ''
for i in range(0, len(list_uncode), 5):
	text_small = text_small + list_uncode[i] + list_uncode[i+1] + list_uncode[i+2] + list_uncode[i+3] + list_uncode[i+4]
	position = key.find(text_small)
	text_uncode = text_uncode + alphabet[position]
	text_small = ''

print (text_uncode)