requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'onions']

'''
if 'mushrooms' in requested_toppings:
	print 'Adding mushrooms'
if 'pepperoni' in requested_toppings:
	print 'Adding pepperoni'
if 'extra cheese' in requested_toppings:
	print 'Adding extra cheese'

print 'Finished making your pizza'
'''

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print 'Sorry, we are out of green pepers right now'
	else:
		print 'Adding ' + requested_topping + '.'
print 'Finish'

if requested_toppings:
	for requested_topping in requested_toppings:
		print 'Adding ' + requested_topping
	print 'Finish pizza'
else:
	print ('Are you sure')


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
'pineapple', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print 'Adding ' + requested_topping
    else:
        print 'Sorry nao temos ' + requested_topping
print 'finish again'


