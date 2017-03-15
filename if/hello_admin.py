users = ['igor', 'laisa', 'admin', 'joao', 'pedro']

if users:
	for user in users:
		if 'admin' in user:
			print 'Ola admin, gostaria de ver um relatorio'
		else:
			print 'Welcome ' + user
else:
	print 'Precisamos encontrar usuarios'


current_users = ['john', 'admin', 'laisa', 'ze', 'tera', 'blade', 'soul']
new_users = ['JOHN', 'laisa', 'admin', 'sera']

for new_user in new_users:
	if new_user.lower() in current_users:
		print new_user + ' Forneca um novo nome, please'
	else:
		print 'Nome ' + new_user + ' esta disponivel'


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
	if number == 1:
		print '1st'
	elif number == 2:
		print '2nd'
	elif number == 3:
		print '3rd'
	elif number == 4:
		print '4th'
	elif number == 5:
		print '5th'
	elif number == 6:
		print '6th'