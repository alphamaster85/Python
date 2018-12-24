import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
la = 'la'
song = la
counterX = 2
counterY = 2

if x > 1:
	for counterX in range(x-1):
		song = song + '-' + la
		counterX = counterX + 1

if y == 0:
	song = ''
else:
	song = ' ' + song
	if y > 1:
		for counterY in range(y-1):
			song = song + ' ' + song
			counterY = counterY + 1

if z == 1:
	song = song + '!'
else:
	song = song + '.'

print ('Everybody sing a song:' + song)