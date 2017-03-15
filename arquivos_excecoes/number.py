"""Adicao"""

print("Give me two numbers, and I'll sum them.")
print("Enter 'q' to quit")

while True:
	first_number = raw_input('First number: ')
	if first_number == 'q':
		break
	second_number = raw_input('Second number: ')
	if second_number == 'q':
		break

	try:
		soma = int(first_number) + int(second_number)
	except ValueError:
		print("Digite um numero")
	else:
		print(soma)