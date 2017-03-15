peoples = {
	'first_name' : 'Igor',
	'last_name' : 'Dias',
	'age' : 26,
	'country' : 'Brazil'
}

for info, name in peoples.items():
	print 'Informacao: ' + info + ' nome: ' + str(name)

print 'First name: ' + peoples['first_name']
print 'Last name: ' + peoples['last_name']
print 'Age: ' + str(peoples['age'])
print 'Country: ' + peoples['country']


favorite_numbers = {
	'igor' : 32,
	'laisa' : 43,
	'joao' : 3,
	'pedro' : 33,
}

print 'Igor ' + str(favorite_numbers['igor'])
print 'Laisa ' +str(favorite_numbers['laisa'])


glossario = {
	'print' : 'imprimir na tela',
	'var' : 'variavel',
	'sum' : 'somar',
	'while' : 'enquanto',
}

for key, value in glossario.items():
	print 'O significado de ' + key + ' e: ' + value

print '\n'

rios = {
	'nilo' : 'egito',
	'amazonas' : 'amazonas',
	'negro' : 'para',
	'fransisco' : 'brasil'
}

for name, rio in rios.items():
	print 'O ' + name.title() + ' corre pelo ' + rio.title()

print '\n'
for name in rios.keys():
	print name.title()

print '\n'
for rio in rios.values():
	print rio.title()