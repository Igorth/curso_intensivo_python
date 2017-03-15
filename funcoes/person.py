def build_person(first_name, last_name, age=''):
	"""Devolve um dicionario com informacoes sobre uma pessoa"""
	person = {'first' : first_name, 'last' : last_name }

	if age:
		person['age'] = age

	return person

my_name = build_person('igor', 'dias', age=26)
print(my_name)