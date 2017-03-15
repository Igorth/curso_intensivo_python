'''
def city_country(cidade, pais):
	info = cidade.title() + ', ' + pais.title()
	return info

informacao = city_country('santiago', 'chile')
print(informacao)


def make_album(name, titulo, number_faixas=''):

	album = {'nome' : name, 'titulo' : titulo}
	
	if number_faixas:
		album['numero da faixa'] = number_faixas
	
	return album

musician = make_album('igor', 'cd', number_faixas=33)
print(musician)

'''

def make_album_two(name, titulo, number_faixas=''):

	album = {'nome' : name, 'titulo' : titulo}
	
	if number_faixas:
		album['numero da faixa'] = number_faixas
	
	return album

while True:
	print('Albuns: ')
	print('Quando quiser sair, digite "q"')
	name_album = raw_input('Digite o nome: ')
	if name_album == 'q':
		break
	titulo_album = raw_input('Digite o titulo:')
	if titulo_album == 'q':
		break
	number_album = raw_input("Digite o numero de faixas: ")
	if number_album == 'q':
		break

	full_info = make_album_two(name_album, titulo_album, number_album)
	print(full_info)