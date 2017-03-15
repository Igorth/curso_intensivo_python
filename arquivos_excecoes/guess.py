name = raw_input('Say your name: ')

filename = 'guess.txt'

with open(filename, 'a') as file_object:
	file_object.write(name.title() + '\n')