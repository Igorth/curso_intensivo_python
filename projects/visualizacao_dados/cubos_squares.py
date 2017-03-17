import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Definie o título do gráfico e nomeia os eixos
plt.title("Cubos Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubo of Value", fontsize=14)

# Define o tamanho dos rótulos das maracações
# plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 5000, 0, 126111000000])

plt.show()