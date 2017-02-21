'''
dimensions = (200, 50)
#dimensions[0] = 250 #'tuple' object does not support item assignment
print dimensions[0]
print dimensions[1]

for dimension in dimensions:
    print dimension

print 'Original dimensions:'
for dimension in dimensions:
    print dimension

dimensions = (400, 100)
print '\nModified dimensions:'
for dimension in dimensions:
    print dimension
'''

plates = ('tropeiro', 'ovo', 'feijoada', 'omelete', 'peixe')
for plate in plates:
    print 'Esse e um prato:' + plate

plates = ('tropeiro', 'arroz', 'feijao', 'carne', 'peixe')
for plate in plates:
    print '\nMudou o cardapio:' + plate


plates[0] = 'arroz'
print plates
