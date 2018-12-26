import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
la = 'la'
song = la
sing = ''

if x > 1:
	for counter in range(x-1):
		song = song + '-' + la

if y == 0:
	sing = ''
else:
	sing = song
	if y > 1:
		for counter in range(y-1):
			sing = sing + ' ' + song
	sing = ' ' + sing

if z == 1:
	sing = sing + '!'
else:
	sing = sing + '.'

print ('Everybody sing a song:' + sing)