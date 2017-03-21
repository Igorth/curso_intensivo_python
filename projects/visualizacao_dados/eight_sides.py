import pygal
from die import Die

# Cria dois D8
die_1 = Die(8)
die_2 = Die(8)

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000 times"
hist.x_labels = []
for item in range(2, 17):
	hist.x_labels.append(item)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('eight_sides.svg')


