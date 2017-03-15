# cria uma lista vazia par armazenar alienigenas
aliens = []

# cria 30 alienigenas verdes
for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'


#Mostra os 5 primeiros aliens
for alien in aliens[:5]:
	print alien

print '...'

# Mostra quantos aliens foram criados

print 'Total number of aliens: ' + str(len(aliens)) 


'''
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print alien


new_points = alien_0['points']
print 'You just earned ' + str(new_points) + ' points'

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print alien_0


alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print alien_0

alien_0 = {'color' : 'green'}
print 'The alien is ' + alien_0['color']

alien_0['color'] = 'yellow'
print 'The alien is now ' + alien_0['color']

del alien_0['points']
print alien_0


alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print 'Origianl x-postion ' + str(alien_0['x_position'])

# Move o alienigena para a direita
# Determina a disntancia que o alienigena deve se deslocar de acordo com sua
# velocidade atual
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# Este deve ser um alienigena rapido
	x_increment = 3

# A nova posicao e a posicao antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print 'New x-position: ' + str(alien_0['x_position'])

'''