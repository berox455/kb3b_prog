def je_druha_mocnina(n):
    i = 0

    if n == 1: return True

    while n/2 > i:
        if i*i == n:
            return True
        i += 1

    return False


def mocnina_sumy(n):
    vysledek = 0
    i = 0

    while n >= i:
        vysledek += i

        i += 1

    return vysledek*vysledek


def soucet_nizsich_mocnin(n, e):
    i = 0
    hodnota = 0
    
    while n >= i:
        hodnota += i**e
        i += 1
    
    return hodnota


n = int(input("Zadej cislo: "))

print(soucet_nizsich_mocnin(n, 4))
