pokracovat = True
soucet = 0
i = 0

while pokracovat:
    vstup = int(input("Zadej cislo: "))
    soucet +=vstup
    
    if vstup == 0:
        if soucet == 0:
            print("Prumer=", i)
        else:
            print("Prumer=", soucet/i)
        pokracovat = False
    else:
        i+=1