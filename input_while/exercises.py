'''
prompt = '\nDigite os ingredientes da pizza: '
prompt += '\nEnter "quit" when you are finished. '

active = True

while active:
	pizza = raw_input(prompt)

	if pizza == 'quit':
		active = False
	else:
		print 'Irei acrescentar ' + pizza

'''

prompt = raw_input('\nQual a sua idade? ')
prompt = int(prompt)

if prompt <= 3:
	print 'Gratuito'
elif prompt > 3 and prompt < 12:
	print '10 dolares'
elif prompt >= 12:
	print '15 dolares'
