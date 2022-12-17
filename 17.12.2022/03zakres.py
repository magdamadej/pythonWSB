zmienna_z_zakresu_globalnego = 30
print(zmienna_z_zakresu_globalnego * 2)

def dodaj_liczby(liczba):
    global zmienna_z_zakresu_lokalnego
    zmienna_z_zakresu_lokalnego = 20

    suma = zmienna_z_zakresu_lokalnego + liczba
    print(f"Suma: {suma}")
    print(f"Zmienna lokalna: {zmienna_z_zakresu_lokalnego}")
    print(f"Zmienna globalna: {zmienna_z_zakresu_globalnego}")

dodaj_liczby(5)
print(zmienna_z_zakresu_lokalnego)