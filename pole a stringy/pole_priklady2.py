def je_serazene(pole):
    cislo = 0
    delka_pole = len(pole) - 1
    
    for cislo in range(delka_pole):
        if pole[cislo] > pole[cislo+1]:
            return False

    return True
    

def smaz_suda(pole):
    pole_kopie = pole.copy()

    for cislo in pole_kopie:
        if cislo % 2 == 0:
            pole.remove(cislo)
    
    return pole


def smaz_duplikaty(pole):
    pole_kopie = pole.copy()
    pole_kopie.sort()
    delka = len(pole_kopie)

    for cislo in range(delka):
        if pole_kopie[cislo] == pole_kopie[cislo-1]:
            pole.remove(pole_kopie[cislo])

    return pole


def vypocti_median(pole):
    kopie_pole = pole.copy()
    kopie_pole.sort()

    n = len(kopie_pole)

    if n % 2 == 0:
        y = (n+2) / 2
        x = n / 2
        median = (kopie_pole[int(y-1)] + kopie_pole[int(x-1)]) / 2
        return median
    else:
        y = (n+1)/2
        return kopie_pole[int(y - 1)]

pole = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 14, 8]
pole1 = [2, 5, 1, 1, 25, 5, 5]
pole2 = [1, 2, 3, 4, 8, 12, 20, 21, 22, 25]
#print(je_serazene(pole))
#smaz_suda(pole)
#smaz_duplikaty(pole1)

#print(pole)

print(vypocti_median(pole))