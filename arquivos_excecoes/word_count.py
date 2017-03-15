def count_words(filename):
	"""Conta o numero aproximado de palavras em um arquivo."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + ' does not exist.'
		print(msg)
	else:
		# Conta o numero aproximado de palavras no arquivo
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'difsa.txt', 'programming.txt', 'guess.txt']
for filename in filenames:
	count_words(filename)