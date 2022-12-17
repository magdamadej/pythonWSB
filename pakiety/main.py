from pakiet_wzorow import modul_pola_figur, modul_objetosci_bryl

print("Obliczanie pola kwadratu i objęctości sześcianu o podanym boku")

bok = int(input("podaj długość boku: "))
if bok > 0:
    pole_kwadratu = modul_pola_figur.pole_kwadratu(bok)
    print(f"Pole kwadratu wynosi: {pole_kwadratu}")

    objetosc_szescianu = modul_objetosci_bryl.objetosc_szescianu(bok)
    print(f"Objętość sześcianu wynosi: {objetosc_szescianu}")
    

