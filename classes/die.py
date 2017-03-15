from random import randint

class Die():
	"""Uma classe que pode ser representar um dado."""
	def __init__(self, sides=6):
		"""Inicializa os atributos da classe Die."""
		self.sides = sides

	def roll_die(self):
		"""Exibe um número aleatório."""
		x = randint(1,self.sides)
		print('My number is: ' + str(x))


my_roll = Die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()
my_roll.roll_die()

my_sort_rol = Die(10)
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()
my_sort_rol.roll_die()

my_sort_sort_roll = Die(20)
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()
my_sort_sort_roll.roll_die()