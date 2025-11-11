def sudlich(string):
    for i in range(0, len(string)):
        if i % 2 == 0:
            print(string[i], end="")
    
    for i in range(0, len(string)):
        if i % 2 != 0:
            print(string[i], end="")


def prum_zmena(pole):
    zmena_soucet = 0 #pro mezivypocet
    delka = len(pole) - 1

    
    if delka == 0: #pokud neni mezi cim by se zmena hledala
        return None
    else:
        for cislo in range(delka):
            zmena_soucet += pole[cislo+1] - pole[cislo]

        return zmena_soucet/delka


def limiter(pole, limit):
    copy_pole = pole.copy()
    copy_pole.sort()

    for cislo in copy_pole:
        if cislo <= limit:
            pole.remove(cislo)

