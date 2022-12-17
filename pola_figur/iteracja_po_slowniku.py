wyniki = {
    'kwadrat' : [20, 56],
    'prostokat' : [41, 56, 45, 78],
    'trapez' : [5],
}

print(wyniki.keys())
print(wyniki['kwadrat'])
print(wyniki['prostokat'])
print(wyniki['trapez'])

with open('wyniki.txt', 'w') as file:
    for keys in wyniki.keys():
        pola_figur = wyniki[keys]
        print(pola_figur)
        for pole in pola_figur:
            file.write(f"Pole {keys}: {pole} \n")