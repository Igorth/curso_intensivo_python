def read_animals(filename):
	"""Tenta ler o arquivo de animais na pasta."""
	try:
		with open(filename) as file_object:
			contents = file_object.readlines()
			print(contents)
	except FileNotFoundError:
		#print("O arquivo: " + filename + " nao foi encontrado")
		pass

my_animals = ['cats.txt', 'dogs.txt']
for my_animal in my_animals:
	read_animals(my_animal)