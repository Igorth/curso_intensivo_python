"""lista de convidados."""

filename = 'guest_book.txt'


while True:
	name = raw_input('Say your name: ')
	with open(filename, 'a') as file_object:
		file_object.write(name.title() + '\n')

	if name == 'q':
		break