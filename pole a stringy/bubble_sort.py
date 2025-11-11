import time
import random

def je_serazene(pole):  #kontroluje, jestli je pole serazene
    cislo = 0
    delka_pole = len(pole) - 1
    
    for cislo in range(delka_pole):
        if pole[cislo] > pole[cislo+1]:
            return False

    return True


def bubble_sort(pole):  #dela bubble sort na poli
    delka = len(pole)

    while je_serazene(pole) == False:   #dokud pole neni serazene tak provadi bubble sort
        for cislo in range(delka - 1):
            if pole[cislo] > pole[cislo+1]:
                docas = pole[cislo+1]
                pole[cislo+1] = pole[cislo]
                pole[cislo] = docas

    return pole


pole = []
for _ in range(10000):
  pole.append(random.randint(0, 100000000))

start = time.time()

print(bubble_sort(pole))

end = time.time()

print("Delka trvani v sekundach", end - start)