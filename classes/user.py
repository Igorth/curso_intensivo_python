"""Uma classe que pode ser usada para representar um usuário."""

class User():
	"""Informacoes do usuario"""
	def __init__(self, first_name, last_name, cellphone, age):
		"""Inicializa os atributos first_name and last_name."""
		self.first_name = first_name
		self.last_name = last_name
		self.cellphone = cellphone
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		"""Descreve um novo usuario"""
		print('\nPrimeiro nome: ' + self.first_name.title())
		print('\nUltimo nome: ' + self.last_name.title())
		print('\nCelular: ' + str(self.cellphone))
		print('\nIdade: ' + str(self.age))

	def greet_user(self):
		"""Mostra o nome completo da pessoa."""
		full_name = self.first_name + ' ' + self.last_name
		print('Ola, ' + full_name)

	def increment_login_attempts(self):
		"""Soma a quantidade de tentativas de login do usuario."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reseta o número de tentativas de login do usuário."""
		self.login_attempts = 0







'''
my_admin = Admin('igor', 'dias', 323123, 26)
my_admin.privilege.show_privileges()


user = User('laisa', 'agueda', 55555, 22)
my_user = User('Igor', 'dias', 333333, 26)
your_user = User('Pedro', 'silva', 12212, 44)


user.describe_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
print('\n')

user.reset_login_attempts()
print(user.login_attempts)
print('\n')

print(my_user.first_name)
print(my_user.last_name)
print(my_user.cellphone)
print(my_user.age)
my_user.describe_user()
my_user.greet_user()
your_user.describe_user()
your_user.greet_user()
'''