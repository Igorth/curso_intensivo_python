import unittest
from city_country import get_city_country_name

class CitiesTestCountry(unittest.TestCase):
	"""Testes para city_country.py."""

	def test_city_coutry(self):
		"""Verificar se 'santigo' e 'chile' retornam Santiago,Chile."""
		formatted_city = get_city_country_name('santiago', 'chile')
		self.assertEqual(formatted_city, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Verifica a população também, deve retornar Santiago, Chile - população 1234."""
		formatted_city = get_city_country_name('santiago', 'chile', 1234)
		self.assertEqual(formatted_city, 'Santiago, Chile - população 1234')

unittest.main()
