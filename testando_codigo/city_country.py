def get_city_country_name(cidade, pais, population=''):
	"""Gera uma saida Cidade, Pais."""
	if population:
		name = cidade.title() + ', ' + pais.title() + ' - população ' + str(population )
	else:
		name = cidade.title() + ', ' + pais.title()
	return name