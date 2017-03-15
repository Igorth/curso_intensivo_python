def print_models(unprintend_designs, completed_models):
	"""
	Simula a impressao de cada design, ate que nao haja mais nenhum.
	Transfere cada design para completed_models apos a impressao
	"""

	while unprintend_designs:
		current_design = unprintend_designs.pop()

		# Simula a criacao de uma impressora 3D a partir do design
		print('Printing model: ' + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	""" Mostra todos os modelos impressos"""
	print('\nThe following models have been printed: ')
	for completed_model in completed_models:
		print(completed_model)