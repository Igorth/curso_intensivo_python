guests = ['Igor', 'Laisa', 'Joao']
message = 'Gostaria de jantar hoje: ' + guests[0]
print message

dontgo = guests.pop()
mesageleave = 'The guest ' + dontgo + ' dont came'
print mesageleave

guests.insert(2, 'Maria');
newguest = guests.pop()
messageguest = 'The new guest is ' + newguest
print messageguest

print 'I found one table bigger'

guests.insert(0, 'Man')
guests.insert(2, 'Jen')
guests.append('Ken')

print guests

print 'Sorry, people. But I just guest one'

guest1 = guests.pop(0)
guest2 = guests.pop(1)
guest3 = guests.pop(-1)

del guests[0]
del guests[1]

print guests
