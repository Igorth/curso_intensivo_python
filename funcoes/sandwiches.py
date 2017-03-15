def call_sandwiche(*recipes):
	print('\nMontando um sanduiche com: ')
	for recipe in recipes:
		print('- ' + recipe)

call_sandwiche('hamburguer')
call_sandwiche('hamburguer', 'queijo')
call_sandwiche('cebola', 'pao', 'picles', 'tomates', 'carne')


def my_build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last

	for key, value in user_info.items():
		profile[key] = value

	return profile

user_profile = my_build_profile('Igor', 'Laisa', location='Brasil', ocupation='Web Developer')
print('\n')
print(user_profile)


def my_car(name, modelo, **car_info):
	car = {}
	car['fabricante'] = name
	car['modelo'] = modelo

	for key, value in car_info.items():
		car[key] = value

	return car

profile_car = my_car('ferrari', 'f50', location='italy', color='red')
print('\n')
print(profile_car)