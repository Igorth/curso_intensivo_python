'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print 'My favorite foods are:'
print my_foods

print '\nMy friend favorite foods are:'
print friend_foods

print 'As tres primeiras comdias sao:'
for myfood in my_foods[:3]:
    print myfood.title()

print 'Os dois itens do meio sao:'
for myfood in my_foods[1:-1]:
    print myfood

print 'Os tres ultimos digitos da lista sao:'
for myfood in my_foods[-3:]:
    print myfood
'''

'''
pizzas = ['calabresa', 'peperoni', 'sugo']
friend_pizzas = pizzas[:]

pizzas.append('queijo')
friend_pizzas.append('carne')


print 'Minhas pizzas favoritas sao:'
for pizza in pizzas:
    print pizza
print '\n'
print 'As pizzas favoritas do meu amigo sao:'
for pizza in friend_pizzas:
    print pizza
'''
