import json

def get_stored_number():
	"""Procura saber se o nome de usuario ja esta armazenado."""
	filename = 'favorite_numbers.json'
	try:
		with open(filename) as f_obj:
			number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return number


def get_new_number():
	"""Pede um novo numero ao usuario."""
	number = raw_input('Qual e o seu numero favorito?')
	filename = 'favorite_numbers.json'
	with open(filename, 'w') as f_obj:
		json.dump(number, f_obj)
	return number


def greet_number():
	"""Mostrar o numero favorito."""
	number = get_stored_number()
	if number:
		print('Eu sei qual e o seu numero favorito! E: ' + number)
	else:
		number = get_new_number()
		print('Cria um novo numero favorito ' + number)

greet_number()