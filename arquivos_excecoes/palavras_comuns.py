def read_textos(filename):
	"""Tenta ler texto e retornar palavras comuns"""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
			print(contents)
	except FileNotFoundError:
		print("O arquivo: " + filename + " nao foi encontrado")
	else:
		"""Mostra o numero de palavras repetidas."""
		words = contents.lower().count('the')
		print("Palavras 'the' repetidas: " + str(words))
		

my_textos = ['alice.txt']
for my_texto in my_textos:
	read_textos(my_texto)