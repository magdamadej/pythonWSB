word1 = input("Podaj jakieś słowo: ").lower()
zbior_samoglosek = set()

for letter in word1:
    if letter in 'aoeiuyą':
        zbior_samoglosek.add(letter)

print(zbior_samoglosek)