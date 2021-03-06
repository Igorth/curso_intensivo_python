import pygal
from die import Die

# Cria dois dados D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(5000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times"
hist.x_labels = []
for item in range(3, 17):
	hist.x_labels.append(item)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_dice.svg')


