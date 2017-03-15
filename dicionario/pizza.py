# Armazena informacoess sobre uma pizza que esta sendo pedida
pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms', 'extra cheese'],
}

# Resume o pedido
print 'You ordered a ' + pizza['crust'] + ' -crust pizza' + ' with the followin toppings:'

for topping in pizza['toppings']:
	print '\t' + topping