import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Testes para 'name_function.py'."""

	def test_first_last_name(self):
		"""Nomes como 'Janis Joplin' funciona?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Nomes como 'Igor Thadeu Caetano' funcionam?"""
		formatted_name = get_formatted_name('igor', 'caetano', 'thadeu')
		self.assertEqual(formatted_name, 'Igor Thadeu Caetano')

unittest.main()