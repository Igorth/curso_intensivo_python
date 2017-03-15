car = 'subaru'

if car == 'subaru':
	print "Is car == 'subaru'? I predict true"
else:
	print 'Car it doesnt a subaru'

foods = ['carne', 'frango', 'porco', 'peixe']

if 'carne' in foods:
	print 'Estou aqui'
else:
	print 'Nao estou aqui'

times = ['cruzeiro', 'Galo', 'america']

for time in times:
	if time == 'america':
		print time.upper()
	else:
		print time.title()

names = ['igor', 'joao', 'pedro']
myList = []

for name in names:
	myList.append(name.title())
print myList