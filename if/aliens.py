alien_color = 'red'

if alien_color == 'verde':
	print 'Voce acabou de ganhar 5 pontos'

alien_color_two = 'yellow'

if alien_color_two == 'verde':
	print 'Voce acabou de ganhar 5 pontos'
else:
	print 'Voce acabou de ganhar 10 pontos'

if alien_color_two == 'verde':
	print ' Voce ganhou 5 pontos'
elif alien_color_two == 'yellow':
	print 'Voce ganhou 10 pontos'
else:
	print 'Voce ganhou 15 pontos'


age = 26

if age < 2:
	print 'Baby'
elif age < 4:
	print 'Crianca'
elif age < 13:
	print 'Garoto(a)'
elif age < 20:
	print 'Adolescente'
elif age < 65:
	print 'Adulto'
elif age >= 65:
	print 'Idosa'


frutas = ['uva', 'pera', 'banana', 'maca', 'melao']

if 'uva' in frutas:
	print 'Voce realmente gosta de uva'
if 'pfdf' not in frutas:
	print 'Nao esta'
if 'maca' in frutas:
	print 'voce gosta de maca'