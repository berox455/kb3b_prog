def nejvetsi(pole):
    if len(pole) == 0:
        return None
    
    pole.sort()
    return pole[-1]

def kolik_sudych(pole):
    sudych = 0

    for cislo in pole:
        if cislo%2 == 0:
            sudych += 1
    return sudych


def vice_kladnych(pole):
    zaporne = 0

    for cislo in pole:
        if cislo < 0:
            zaporne += 1
    
    return 0.5 * len(pole) > zaporne


def prumerna_odchylka(pole):
    soucet = 0
    odchylka = 0

    for cislo in pole:
        soucet += cislo
    
    prumer = soucet / len(pole)

    for cislo in pole:
        odchylka += abs(cislo - prumer)

    return odchylka / len(pole)


pole1 = [20, 1, 30, 5, -1, 28, 55, 32]
pole = [-1, -2, -3, -4, 20, -30, 44, 70]
pole2 = [200, -1, 444, -3, -5]
pole0: list[int] = []
pole3 = [5, 2, -1, 3, 4, 1, 0, 9]

#print(nejvetsi(pole0))
#print(kolik_sudych(pole))
#print(vice_kladnych(pole2))
print(prumerna_odchylka(pole3))