# python -m pip install matplotlib
# pyplot - moduł zawierający funkcje do tworzenia wykresów

import matplotlib.pyplot as plt

x_values = [i for i in range(0, 10)]
y_values_2 = [x ** 2 for x in x_values]
y_values_3 = [z ** 3 for z in x_values]

fig, ax = plt.subplots()
#fig - cały rysunek (kolekcja wygeberowanych wykresów)
#ax - jeden wykres
#subplots() - pozwala wygenerować jeden lub więcej wykresów na jednym rysunku

ax.plot(x_values, y_values_2, c='red')
ax.plot(x_values, y_values_3, c='green')
#plot() - funkcja generująca wykres liniowy

ax.set_title("Kwadraty liczb", fontsize = 20)
ax.set_xlabel("Liczby")
ax.set_ylabel("Kwadraty i sześciany liczb")

#plt.savefig('funcja.png')
plt.show()