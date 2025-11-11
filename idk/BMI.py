while True:
    m = float(input("\nZadej svoji hmotnost v kg: "))
    v = float(input("Zadej vysku v cm: "))
   
    v/=100
    bmi = round(m/(v*v), 2)

    print("\nBMI: ", bmi)
    if bmi >= 40:
        print("\nObezita 3. stupně morbidní obezita")
    elif bmi >= 35:
         print("\nObezita 2. stupně")
    elif bmi >= 30:
        print("\nObezita 1. stupně")
    elif bmi >= 25:
        print("\nNadváha")
    elif bmi >= 18.5:
        print("\nNormální hmotnost")
    else:
        print("\nPodvýživa")