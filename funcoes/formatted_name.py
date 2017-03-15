'''
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Devolve um nome completo formatado de modo elegante"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()


second = get_formatted_name('laisa', 'agueda')
musician = get_formatted_name('igor', 'dias', 'caetano')

print(musician)
print(second)
'''

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Devolve um nome completo formatado de modo elegante"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

# Este e um loop infinito
while True:
	print('\nPlease tell me your name: ')
	print('Enter "q" at any time to quit')
	f_name = raw_input('First name: ')
	if f_name == 'q':
		break
	l_name = raw_input('Last name: ')
	if l_name == 'q':
		break
	m_name = raw_input('Middle name: ')
	if m_name == 'q':
		break

	formatted_name = get_formatted_name(f_name,l_name, m_name)
	print('\nHello, ' + formatted_name)