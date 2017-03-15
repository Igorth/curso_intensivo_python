people_0 = {
	'first_name' : 'Igor',
	'last_name' : 'Dias',
	'age' : 26,
	'country' : 'Brazil'
}

people_1 = {
	'first_name' : 'Laisa',
	'last_name' : 'Agueda',
	'age' : 28,
	'country' : 'Brazil'
}

people_2 = {
	'first_name' : 'Pedro',
	'last_name' : 'Xavier',
	'age' : 26,
	'country' : 'NZ'
}

peoples = [people_0, people_1, people_2]

for people in peoples:
	fullname = people['first_name'] + ' ' + people['last_name']
	age = people['age']
	country = people['country']
	print '\nFull name: ' + fullname
	print '\t Idade: ' + str(age)
	print '\t Country: ' + country


cao = {
	'tipo' : 'cachorro',
	'raca' : 'vira lata'
}

gato = {
	'tipo' : 'garfield',
	'raca' : 'grande',
}

coelho = {
	'tipo' : 'pernalonga',
	'raca' : 'desenho',
}

pets = [cao, gato, coelho]

for pet in pets:
	tipo = pet['tipo']
	raca_a = pet['raca']
	print tipo
	print raca_a
