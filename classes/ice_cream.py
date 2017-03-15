"""Uma classe que pode representar uma sorveteria."""

from restaurant import Restaurant

class IceCreamStand(Restaurant):
	"""Representa uma sorveteria que tem em um restaurante."""
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializa os atributos da classe-pai."""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['morango', 'uva', 'flocos', 'coco']

	def show_flavors(self):
		"""Mostra os sabores do sorvete."""
		for flavor in self.flavors:
			print('Os sabores que temos: ' + flavor)



restaurant = Restaurant('comidaria', 'massas')
restaurant.describe_restaurant()
restaurant.number_served = 50
restaurant.set_number_served()
restaurant.increment_number_served(33)
restaurant.set_number_served()

my_icecream = IceCreamStand('django', 'mexicanas')
my_icecream.describe_restaurant()
my_icecream.show_flavors()