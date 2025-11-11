while 1==1:
    a = float(input("\nZadej 1. cislo: "))
    b = float(input("Zadej 2. cislo: "))
    c = float(input("Zadej 3. cislo: "))

    if a == b == c:
        print("Vsechna cisla jsou stejna")
    elif (a < b and b <= c) or (a < c and c <= b) or (a < b and a <= c):
        print("Nejmensi cislo je: ", a)
    elif (b < a and a <= c) or (b < c and b <= a) or (b < a and b <= c):
        print("Nejmensi cislo je: ", b)
    elif (c < a and a <= b) or (c < b and b <= a) or (c < a and c <= b):
        print("Nejmensi cislo je: ", c)
    else:
        print("neco se pokazilo")