print(chr(85))
print(ord("M"))

print('-' * 20)
a = -9
print(f"Wartośc bezwzględna z liczby {a} wynosi: {abs(a)}")

print('-' * 20)
b = 5.551256325478
c = round(b, 3)
print(round(b, 3))
print(b)
print(c)

print('-' * 20)
names = ["Adam", "Juliusz", "Jan", "Czesław"]
last_names = ["Mickiewicz", "Słowacki", "Brzechwa", "Miłosz"]
years = [1855, 1849, 1966, 2004]

print(list(zip(names, last_names, years)))

for i, poet in enumerate(list(zip(names, last_names, years)), start=1):
    print(f"Poeta {i}: {poet[0]} {poet[1]}. Zmarł w roku: {poet[2]}")

print("-" * 20)
countries = ['Polska', 'USA', 'Francja', 'Argentyna', 'Maroko', 'Chorwacja']

for i, country in enumerate(countries, start=1):
    print(i, country)


print(pow(9, 2))
