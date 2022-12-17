def witaj():
    name = input("Podaj imię: ").capitalize()
    print(f"Witaj {name}")
# witaj()


def witaj2 (name: str):
    print(f"Witaj {name.capitalize()}")
witaj2("ola")
witaj2("ala")

def suma(number_1: float, number_2: float):
    suma_liczb = number_1 + number_2
    print(f"Suma liczb {number_1} i {number_2} wynosi: {suma_liczb}")

suma(56, 89)
suma(45, 85)
suma(1203, 12548)

def suma1(number_1 = 1, number_2 = 2):
    suma_liczb = number_1 + number_2
    print(f"Suma liczb {number_1} i {number_2} wynosi: {suma_liczb}")

    if number_1 > 100:
        return suma_liczb
    else:
        return suma_liczb + suma_liczb
        print("HAHAHA")

suma1()
suma1(10)
suma1(10, 20)
# suma1(10, 20, 30)

sum1 = suma1(50, 150)
print(sum1)

def test_args(x: int, *numbers):
    print(f"Pierwsza liczba: {x}")
    for num in numbers:
        print(f"Kolejna liczba z tupli numbers: {num}")

test_args(5)
test_args(5,6,5,8,9,5,6,5,58,4,6,5,5,5,6,5,5)


def srednia(*numbers):
    return sum(numbers) / len(numbers)

srednia_zmienna = srednia(5,4,8,4,7,9,5,2,3,6,4,5,6,7,89,4)
print(srednia_zmienna)