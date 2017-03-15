def describe_pet(pet_name, animal_type='dog'):
	"""Exibe informacoes sobre um animal de estimacao"""
	print('\nI have a ' + animal_type)
	print('My ' + animal_type + "'s name is " + pet_name.title())

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
# describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='terere')
describe_pet('auau')
describe_pet('tere', 'cat')
#describe_pet()

def make_shirt(tamanho='grandes', texto='Eu amo python'):
	print('\nTamnho da camisa: ' + tamanho)
	print('\tFrase da camisa: ' + texto)

make_shirt('pequena', 'ola mundo')
make_shirt(tamanho='media', texto='hello world')
make_shirt()
make_shirt(tamanho='pequena', texto='outra frase')


def describe_city(cidade, pais='Brazil'):
	print('\n' + cidade.title() + ' esta localizada no ' + pais)

describe_city('bh')
describe_city(cidade='aloha')
describe_city(pais='NZ', cidade='Auck')
describe_city('fdsa', 'olds')
