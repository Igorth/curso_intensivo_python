'''
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'C',
	'igor' : 'ruby',
	'phil' : 'python',
}


if 'erin' not in favorite_languages.keys():
	print 'Erin, please take our poll'

print "Sarah's favorite language is " + favorite_languages['sarah'].title()

for name, language in sorted(favorite_languages.items()):
	print name.title() + "'s favorite language is " + language.title()

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print name.title()

	if name in friends:
		print 'Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title()

print 'The following languages have been mentioned:'
for language in sorted(set(favorite_languages.values())):
	print language.title()

participantes = ['pedro', 'laisa', 'sofia', 'igor']
for name in favorite_languages.keys():
	if name in participantes:
		print 'Parabens ' + name + ' voce participou da enquete'

'''


favorite_languages = {
	'jen' : ['python', 'ruby'],
	'sarah' : ['C'],
	'igor' : ['ruby', 'java'],
	'phil' : ['python', 'haskel'],
}

for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print '\n' + name.title() + ' your favorite language is:'
	else:
		print '\n' + name.title() + ' your favorite languages are: '

	for  language in languages:
		print '\t' + language