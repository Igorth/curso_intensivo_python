def make_great(username, modificada_listas):
	while username:
		current_name = username.pop()
		print('\n' + current_name)
		modificada_listas.append(current_name)


def show_magicians(modificada_listas):
	for modificada_lista in modificada_listas:
		print('\nO grande ' + modificada_lista.title())



username = ['igor', 'laisa', 'sofia', 'pedro']
modificada_listas = []

#make_great(username, modificada_listas)
make_great(username[:], modificada_listas)
show_magicians(modificada_listas)

print(username)