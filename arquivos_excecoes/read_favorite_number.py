import json

filename = 'favorite_numbers.json'

with open(filename) as f_obj:
	numbers = json.load(f_obj)

print('Eu sei qual e o seu numero favorito! E: ' + numbers)