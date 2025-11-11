correct = True

while correct:
    cislo = int(input("Zadej kladne trimistne sude cislo: "))
    
    if cislo < 0:
        print("Zadal jsi zaporne cislo!!\n")
    elif 99 > cislo or cislo > 999:
        print("Nezadal jsi trimistne cislo!!\n")
    elif cislo%2 > 0:
        print("Zadal jsi liche cislo!!\n")
    else:
        print("Zadal jsi spravne cislo")
        correct=False