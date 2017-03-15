car = raw_input('Qual tipo de carro deseja alugar?')
print('Deixe me ver se consigo um ' + str(car) + ' para voce.')

dinner = raw_input('Quantas pessoas estao em seu grupo para jantar?')
dinner = int(dinner)

if dinner > 8:
	print 'Por favor, esperem uma mesa'
else:
	print 'Sua mesa esta pronta'

number = raw_input('Digite um numero: ')
number = int(number)

if number % 10 == 0:
	print 'divisivel'
else:
	print 'nao divisivel'