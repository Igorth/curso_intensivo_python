responses = {}

# Define uma flag para indicar que a enquete esta ativa
polling_active = True

while polling_active:
	# Pede o nome da pessoa e a resposta
	name = raw_input('\nWhat is yout name? ')
	response = raw_input('\nWhich mountain would you like to climb someday? ')

	# Armazena a resposta no dicionario
	responses[name] = response

	# Descobre se outra pessoa vai responder a enquete
	repeat = raw_input('Would you like to let another person respond? (yes/no) ')
	if repeat == 'no':
		polling_active = False

# A enquete foi concluida. Mostra os resultados
print(responsesf)
print('\n--- Poll Results ---')
for name, response in responses.items():
	print(name + ' would like to climb ' + response + '.')