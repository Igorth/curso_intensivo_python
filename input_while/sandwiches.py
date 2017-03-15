sandwich_orders = ['pastrami', 'atum', 'carne', 'pastrami', 'frango', 'tudao', 'pastrami']
print('Nossos sanduiches são: ' + str(sandwich_orders))
finished_sandwiches = []

print('\nSorry, mas acabou o sanduiche de pastrami')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwiches = sandwich_orders.pop()

	print('\nPreparei seu sanduiche de ' + current_sandwiches)
	finished_sandwiches.append(current_sandwiches)

print('\nSanduiches preparados: ')
for finished_sandwiche in finished_sandwiches:
	print('\t' + finished_sandwiche)


