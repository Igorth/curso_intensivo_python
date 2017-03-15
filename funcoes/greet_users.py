def greet_users(names):
	"""Exibe um saudacao simples a cada usuario da lista."""
	for name in names:
		msg = 'Hello ' + name.title()
		print(msg)

username = ['igor', 'laisa', 'pedro']
greet_users(username)