'''
for value in range(1,6):
    print value

numbers = [value for value in range(1,6)]
print numbers

numbers = list(range(1,6))
print numbers

even_numbers = list(range(2,11,2))
print even_numbers

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print squares

# List comprehesions
squares = [value**2 for value in range(1,11)]
print squares

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print min(digits)
print max(digits)
print sum(digits)

#contanto até 20
for value in range(1,21):
    print value
#múmero impares
for value in range(1,21,2): 
    print value
#multiplos de 3
for value in range(3,30,3):
    print value

'''
#calcular o valor ao cubo
cubos = []
for value in range(1,11):
    cubo = value**3
    cubos.append(cubo)
print(cubos)

 #usando o list comprehesions para calcular o cubo
cubos = [value**3 for value in range(1,11)]
print(cubos)
