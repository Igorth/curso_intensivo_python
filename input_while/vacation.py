vacations = {}

vacation_active = True

while vacation_active:
	name = raw_input('\nQual o seu nome? ')
	vacation = raw_input('\nSe pudesse visitar um lugar do mundo, para onde iria? ')

	vacations[name] = vacation

	verificar = raw_input('\nDeseja fazer a pesquisa novamente (yes/no)')
	if verificar == 'no':
		vacation_active = False

print('\n--- Vacations ---')
for name, vacation in vacations.items():
	print(name + ' quer ir para: ' + vacation)