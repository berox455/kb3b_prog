import random
import os

#os.chdir("C:/Users/Home/OneDrive - Střední škola informatiky, poštovnictví a finančnictví Brno/KB3B/Prog/Python/Projekt/wordle upgrade")
file_path = "words.txt"

yellow_bg = "\x1b[48;2;255;255;90m{}\x1b[0m"
green_bg = "\x1b[48;2;0;255;90m{}\x1b[0m"

def word_array(file_path: str) -> list[str]: #generuje nahodne slovo
    with open(file_path, "r") as file:
        words = (file.read()).split(",")
    
    words = [word.strip() for word in words]
    return words


def rand_word() -> str:
    return random.choice(word_array(file_path))

def intro(): #generuje intro ke hre
    print("\n\n-----------------------------------------------------------------------------------------------------")
    print("Toto je wordle, hadas 5 pismena anglicka slova, mas 6 pokusu")
    print("Funguje to tak, ze napises svoje 5 pismene slovo a pote se ti ukaze jake pismena jsi uhodl ", end="") 
    print(green_bg .format("ZELENE"))
    print("Pokud uhodnes pismeno ale je na spatne pozici, zvyrazni se ", end="") 
    print(yellow_bg .format("ZLUTOU"))
    print("Pokud neuhodnes pismeno, tak se s nim nic nestane (proste se normalne vypise)")
    print("-----------------------------------------------------------------------------------------------------\n\n")


def ask_for_slovo() -> str:
    slovo = input("Zadej slovo, ktere ches hadat: ")
    return slovo.upper()


def dictionary_check(slovo: str) -> bool:
    slovo = slovo
    
    #while slovo not in word_array(file_path):
    #    print("Slovo se nenachazi ve slovniku, zkus to znovu")
    #    slovo = ask_for_slovo()
    
    #assert slovo in word_array(file_path), "dictionary_check doesn't work anymore"
    
    return slovo in word_array(file_path)


def get_slovo() -> str: #ziskava slovo od uzivatele
    slovo = ask_for_slovo()

    while slovo.isalpha() == False or len(slovo) != 5 or dictionary_check(slovo) != True:
        if slovo.isalpha() == False:
            print("Spatny input")
        if len(slovo) != 5: 
            print("Delka: ", len(slovo), ", ale ma byt 5", sep="")
        if dictionary_check(slovo) != True:
            print("Slovo se nenachazi ve slovniku, zkus to znovu")
        slovo = ask_for_slovo()

    return slovo


def word_check(word: str, slovo: str) -> None: #zjistuje jestli jsou znaky v nahodne generovanem slovu a potom je vypise
    number = 0

    print("\t\t", end="")

    for pismeno in slovo:
        if slovo[number] in word[number]:
            print(green_bg .format(pismeno), end="")

        else:
            if pismeno in word:
                print(yellow_bg .format(pismeno), end="")

        number += 1

        if pismeno not in word:
            print(pismeno, end="")

    print()


def outro_good(word: str, pokusy: int) -> None:  #print pokud jsi vyhral
    print("Konec hry")
    print("Gratuluji zvladl jsi uhodnout slovo ", word, " na ", pokusy, ". pokus\n\n", sep="")


def outro_bad(word): #print pokud jsi prohral
    print("Konec hry")
    print("Slovo", word, "jsi ani za 6 pokusu neuhadl\n\n")


def play_again() -> bool: #pta se jestli chce hrat znovu
    again = input("Hrat znovu? [a], [n]: ").lower()

    while again != "a" and again != "n":
        print("Spatny input")  
        again = input("Hrat znovu? [a], [n]: ").lower()

    if again == "a":
        return True
    elif again == "n":
        return False


def process() -> None: #process generovani hry
    word = rand_word()

    for pokusy in range(1, 7):
        slovo = get_slovo()
        
        print("Pokus ", pokusy, ":\t\t", sep="", end="")
        word_check(word, slovo)

        #print(word) #debug

        if slovo == word:
            outro_good(word, pokusy)
            break

    if slovo != word:
        outro_bad(word)
    

def hra() -> None: #samotna hra
    intro()
    process()

    while play_again():
        process()
    
    print("Diky za hrani moji verze hry wordle v pythonu")


hra() #spousti hru dughhhh