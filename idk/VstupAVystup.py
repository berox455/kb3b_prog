i = 0
while 0==0:
    vstup = input("Zadej [p] pro papouska a [a] pro pozdrav: ") [0]
    if vstup == "p":
        text = input("Zvolil jsi si papouska, zadej vstup: ")
        while i < 3:
            print(text)
            i += 1
    elif vstup == "a":
        jmeno = input("Zvolil jsi si pozdrav, zadej svoje jmeno: ")
        print("Ahoj", jmeno)
    else:
        print("Spatny vstup")