#pole kwadratu:
def licz_pole_kwadratu(bok: float):
    pole = bok ** 2
    return pole

#pole prostokata
def licz_pole_prostokata(bok_1: float, bok_2: float):
    pole = bok_1 * bok_2
    return pole

#pole trapezu
def licz_pole_trapezu(podstawa_1: float, podstawa_2: float, wysokosc: float):
    pole = round(((podstawa_1 + podstawa_2) * wysokosc) / 2, 2)
    return pole


def licz_pola_figur(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        return (args[0] + args[1]) * args[2] / 2
        

print(licz_pola_figur())

