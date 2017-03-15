"""Uma classe que representa os privilegios de um administrador."""

from user import User

class Privileges():
	"""Tentativa de modelar os privilegios do Administrador."""
	def __init__(self, privileges=['can add post', 'can delete post', 'can ban user', 'can edit post']):
		"""Inicializa os atributos da classe."""
		self.privileges = privileges

	def show_privileges(self):
		"""Visualiza os privilegios do Administrador."""
		for privilege in self.privileges:
			print('Privilégios de um administrador: ' + privilege.title())