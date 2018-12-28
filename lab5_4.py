folder1 = ['C:', 'backup.log', 'ideas.txt']
filename1 = 'ideas.txt'
folder2 = [ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py']
filename2 = 'find.me'
folder3 = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
filename3 = 'hereiam.py'

def file_search(folder, filename):
	way = filename

	for elem in folder:
		if elem == filename:
			return str(folder[0]) + '/' + way
		elif isinstance(elem, list) and len(elem) > 1:
			is_False = file_search(elem, filename)
			if is_False == False:
				return False
			else:
				return str(folder[0]) + '/' + str(file_search(elem, filename))

	return False

print (file_search(folder1, filename1))
print (file_search(folder2, filename2))
print (file_search(folder3, filename3))