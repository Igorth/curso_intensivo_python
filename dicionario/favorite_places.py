favorite_places = {
	'igor' : ['NZ', 'Brazil'],
	'laisa' : ['NZ', 'Bonito', 'Paris'],
	'pedro' : ['Japao'],
	'maria' : ['Africa', 'Tanzania'],
}

for name, places in favorite_places.items():
	if len(places) == 1:
		print '\n' + name.title() + ' meu lugar favorito:'
	else:
		print '\n' + name.title() + ' meus lugares favoritos:'

	for place in places:
		print '\t' + place.title()


favorite_numbers = {
	'igor' : [3, 11, 2, 4],
	'laisa' : [2, 22, 10],
	'pedro' : [5, 10, 3, 23],
	'sofia' : [9]
}

for name, numbers in favorite_numbers.items():
	if len(numbers) == 1:
		print '\n' + name.title() + ' meu numero favorito e:'
	else:
		print '\n' + name.title() + ' meus numeros favoritos sao'

	for number in numbers:
		print '\t' + str(number)



cities = {
	'Auckland' : {
		'country' : 'NZ',
		'population' : 321312,
		'fact' : 'beautiful',
	},
	'Bonito' : {
		'country' : 'Brazil',
		'population' : 312312312,
		'fact' : 'big',
	},
	'Tokio' : {
		'country' : 'Japao',
		'population' : 5455454,
		'fact' : 'clean',
	},
}

for name, name_info in cities.items():
	print '\nNome da cidade: ' + name

	countr = name_info['country']
	populati = name_info['population']
	fac = name_info['fact']

	print '\tPais: ' + countr
	print '\tPopupalacao: ' + str(populati)
	print '\tFato: ' + fac





