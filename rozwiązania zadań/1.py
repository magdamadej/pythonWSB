liczby_dodatnie = []

while len(liczby_dodatnie) < 10:
    liczba = int(input('podaj liczbę: '))
    if liczba > 0:
        liczby_dodatnie.append(liczba)
        
print('największa wartość', max(liczby_dodatnie))
print('najmniejsza wartość', min(liczby_dodatnie))