while True:
    maxp = float(input("\nZadej maximalni pocet bodu testu: "))
    myp = float(input("Zadej tvuj pocet bodu v testu: "))
    
    p = myp/maxp * 100

    print("\nVysledek: ", p, "%", sep="")
    if p >= 90:
        print("\nZnamka: 1")
    elif p >= 75:
         print("\nZnamka: 2")
    elif p >= 60:
        print("\nZnamka: 3")
    elif p >= 30:
        print("\nZnamka: 4")
    else:
        print("\nZnamka: 5")