"""Uma classe que pode ser usada para representar um restaurante."""

class Restaurant():
	"""Primeira classe em python do Restaurante"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializa os atributos restaurant_name e cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Descreve o restaurante"""
		print('\nName of restaurant ' + self.restaurant_name.title())
		print('\tCuisine Type ' + self.cuisine_type.title())

	def open_restaurant(self):
		"""Informa se o restaurante esta aberto."""
		print('O restaurante ' + self.restaurant_name.title() + ' esta aberto')

	def set_number_served(self):
		"""Informa o numero de clientes atendidos pelo restaurante."""
		print('\nNúmero de atendimentos: ' + str(self.number_served))

	def increment_number_served(self, number):
		"""Soma a quantidade de pessoas que visitaram o restaurante."""
		self.number_served += number