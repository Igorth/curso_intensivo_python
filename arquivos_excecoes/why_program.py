"""Enquete sobre programacao"""

filename = 'why_program.txt'

flag = True

while flag:
	text = raw_input('Porque voce gosta de programar?')
	with open(filename, 'a') as file_object:
		file_object.write(text + '\n')

	if text == 'quit':
		flag = False