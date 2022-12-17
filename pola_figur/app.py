#import całego modułu functions
#import functions

#import wybranych funkcji z modułu functions
# from functions import licz_pole_kwadratu, licz_pole_prostokata, licz_pole_trapezu

from functions import licz_pola_figur

start = True

wyniki = {
    'kwadrat' : [],
    'prostokat' : [],
    'trapez' : [],
}

def co_chcesz_zrobic(opcja):

    if opcja == 'tak' or opcja == 't':
        print("Podaj figurę, której pole chcesz policzyć: \n\t1. kwadrat\n\t2. prostokąt\n\t3. trapez")
        wybor_figury = input("Podaj numer figury lub nazwę: ").lower()
        if wybor_figury == "kwadrat" or wybor_figury == "1" or wybor_figury == "1.":
            bok_kwadratu = float(input("Podaj długość boku: "))
            if bok_kwadratu > 0:
                pole_kwadratu = licz_pola_figur(bok_kwadratu)
                print(f"Pole kwadratu wynosi: {pole_kwadratu}")
                wyniki['kwadrat'].append(pole_kwadratu)
        elif wybor_figury == "prostokąt" or wybor_figury == "prostokat" or          wybor_figury == "2" or wybor_figury == "2.":
            bok_1 = float(input("Podaj długość pierwszego boku: "))
            bok_2 = float(input("Podaj długość drugiego boku: "))
            if bok_1 > 0 and bok_2 > 0:
                pole_prostokata = licz_pola_figur(bok_1, bok_2)
                print(f"Pole prostokąta wynosi: {pole_prostokata}")
                wyniki['prostokat'].append(pole_prostokata)    
        elif wybor_figury == "trapez" or wybor_figury == "3" or wybor_figury == "3.":
            bok_1 = float(input("Podaj długość pierwszej podstawy: "))
            bok_2 = float(input("Podaj długość drugiej podstawy: "))
            h = float(input("Podaj długość podstawy: "))
            if bok_1 > 0 and bok_2 > 0 and h > 0:
                pole_trapezu = licz_pola_figur(bok_1, bok_2, h)
                print(f"Pole trapezu wynosi: {pole_trapezu}")
                wyniki['trapez'].append(pole_trapezu)
        else:
            print("Nie znam takiej figury")

    elif opcja == 'nie' or opcja =='n':
        global start
        start = False
    
print(wyniki.keys())
print(wyniki['kwadrat'])
print(wyniki['prostokat'])
print(wyniki['trapez'])

while start:
    opcja = input("czy chcesz uruchomić program? (tak/nie): ").lower()
    co_chcesz_zrobic(opcja)

with open('wyniki.txt', 'w') as file:
    for keys in wyniki.keys():
        pola_figur = wyniki[keys]
        for pole in pola_figur:
            file.write(f"Pole {keys}: {pole} \n")

