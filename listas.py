'''
names = ['Igor', 'Joao', 'Pedro']

for item in names:
    message = "Hello " + item + ", how are you?"
    print message


motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles

motorcycles.append('ducati')
print motorcycles

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print motorcycles

motorcycles.insert(0, 'ducati')
print motorcycles

del motorcycles[0]
print motorcycles

del motorcycles[2]
print motorcycles
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles
popped_motorcycke = motorcycles.pop()
print motorcycles
print popped_motorcycke

'''
last_owned = motorcycles.pop()
print "The last motorcycle I owned was a " + last_owned.title() + "."

first_owned = motorcycles.pop(0)
print "The first motorcycle I owned was a " + first_owned.title() + "."


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print motorcycles
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print motorcycles
print "\nA " + too_expensive.title() + " is too expensive for me."
'''
