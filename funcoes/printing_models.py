'''
# Comeca com alguns designs que devem ser impressos
unprintend_designs = ['ihpne', 'android', 'samsung']
completed_models = []

# Simula a impressao de cada design, ate que nao haja mais nenhum
# Transfere cada design para completed_models apos a impressao
while unprintend_designs:
	current_design = unprintend_designs.pop()

	# Simula a criacao de uma impressao 3D a partir do design
	print('Printing model: ' + current_design)
	completed_models.append(current_design)

# Exibe todos os modelos personalizados
print('\nThe following models have been printed: ')
for completed_model in completed_models:
	print(completed_model)
'''

import printing_functions as pf

unprintend_designs = ['iphone', 'android', 'motorola']
completed_models = []

#print_models(unprintend_designs, completed_models)
pf.print_models(unprintend_designs[:], completed_models) #copia da lista
pf.show_completed_models(completed_models)
print(unprintend_designs)