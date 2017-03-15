"""Um conjunto de classes que pode ser usado para representar carros elétricos."""

from car import Car

class Battery():
	"""Uma tentativa simples de modelar uma bateria para um carro elétrico."""
	def __init__(self, battery_size=70):
		"""Inicializa os atributos da bateria."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Exibe uma frase que descreve a capacidade da bateria."""
		print("This car has a " + str(self.battery_size) + '-KWh battery.')

	def get_range(self):
		"""Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = 'This car can go approximately ' + str(range)
		message += ' miles on a full charge'
		print(message)

	def update_battery(self):
		"""Verificar a capacidade da bateria e defini-la com 85 se o valo for diferente."""
		if self.battery_size != 85:
			self.battery_size = 85


class ElectricCar(Car):
	"""Representa aspectos de um carro específicos de veículos elétricos."""

	def __init__(self, make, model, year):
		"""
		Inicializa os atributos da classe-pai
		Em seguida, inicializa os atributos específicos de um carro elétrico
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank():
		"""Carros elétricos não têm tanques de gasolina."""
		print("This car doesn't need a gas tank!")