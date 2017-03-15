from collections import OrderedDict

glossario = OrderedDict()

glossario['print'] = 'imprimir na tela'
glossario['var'] = 'variavel'
glossario['sum'] = 'somar'
glossario['while'] = 'enquanto'


for key, value in glossario.items():
	print('O significado de ' + key + ' e: ' + value)