"""Uma classe que representa um administrador."""

from user import User
from privileges import Privileges

class Admin(User):
	"""Criando uma classe para o administrador."""
	def __init__(self, first_name, last_name, cellphone, age):
		"""Inicializa os atributos da classe-pai."""
		super().__init__(first_name, last_name, cellphone, age)
		self.privilege = Privileges()
