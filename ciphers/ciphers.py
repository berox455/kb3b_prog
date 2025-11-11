alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
def atbasova_sif(text): #funguje na sifrovani i desifrovani textu
    reverse_alphabet = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
    number = 0

    if text.isalpha():
        for pismeno in text.lower():
            for letter in alphabet:
                if alphabet[number] == pismeno:
                    print(reverse_alphabet[number].upper(), end="")
                    number = 0
                    break
                else:
                    number += 1
    else:
        print("To co jsi vlozil musi byt slozeno pouze z pismen anglicke abecedy!! [tyka se atbosovy sifry]")
    print("")
    

def caesarova_sif(text, posun): #zasifruje zpravu
    number = 0

    if posun < 26 and posun > 0 and type(posun) == int:
        for pismeno in text.lower():
            if pismeno not in alphabet:
                print(pismeno, end="")
            else:
                for letter in alphabet:
                    if alphabet[number] == pismeno:
                        if number + posun > 25:
                            print(alphabet[number + posun - 26].upper(), end="")
                        else:
                            print(alphabet[number + posun].upper(), end="")
                        number = 0
                        break
                    else:
                        number += 1
    else:
        print("Spatny posun!! [posun musi mit hodnotu mezi 1 a 25, plus musi byt cele cislo]")

    print("")


def caesarova_desif(text, posun): #desifruje zpravu
    number = 0
    
    if posun < 26 and posun > 0 and type(posun) == int:
        for pismeno in text.lower():
            if pismeno not in alphabet:
                print(pismeno, end="")
            else:
                for letter in alphabet:
                    if alphabet[number] == pismeno:
                        if number - posun < 0:
                            print(alphabet[number - posun + 26].upper(), end="")
                        else:
                            print(alphabet[number - posun].upper(), end="")
                        number = 0
                        break
                    else:
                        number += 1
    else:
        print("Spatny posun!! [posun musi mit hodnotu mezi 1 a 25, plus musi byt cele cislo]")

    print("")


def substitucni_s_cisly_sif(text): #umi sifrovat text na cisla
    number = 0

    if text.isalpha():
        for pismeno in text.lower():
            for letter in alphabet:
                if alphabet[number] == pismeno:
                    print(number+1, end=" ")
                    number = 0
                    break
                else:
                    number += 1
    else:
        print("To co jsi vlozil musi byt slozeno pouze z pismen anglicke abecedy!! [tyka se substitucni sifry s cisly]")
    
    print("")


def substitucni_s_cisly_desif(pole_cisel): #umi desifrovat cisla na text
    pole_spatnych = []

    for cislo in pole_cisel:
        if type(cislo) == int:
            print(alphabet[cislo-1].upper(), end="")
        else:
            pole_spatnych.append(cislo)
    if len(pole_spatnych) > 0:
        print("")
        print("Prvky: ", end="")
        for prvek in pole_spatnych:
            print(prvek, end="")
        print(" v poli nejsou cislo!!", sep="")
    else:
        print("")


#atbasova_sif("gvcg")
#caesarova_sif("hello, how are you doing?", 20)
#caesarova_desif("BYFFI, BIQ ULY SIO XICHA?", 20)
#substitucni_s_cisly_sif("hello")
#substitucni_s_cisly_desif([8, 5, 12, 12, 15, "!"])