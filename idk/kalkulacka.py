while 1==1:
    a = float(input("\n Zadej 1. cislo: "))
    Choice = input("Zadej [p] pro plus, [m] pro minus, [n] pro nasobeni a [d] pro deleni: ") [0]
    b = float(input("Zadej 2. cislo: "))

    p = a+b
    m = a-b
    n = a*b
    d = a/b

    if Choice == "p" or "m" or "n" or "d":
        if Choice == "p":
            print("Vysledek scitani: ", p)
        elif Choice == "m":
            print("Vysledek scitani: ", m)
        elif Choice == "n":
            print("Vysledek scitani: ", n)
        elif Choice == "d":
            print("Vysledek scitani: ", d)
        else:
            print("Spatny input!!")
    else:
        print("Neco se pokazilo")