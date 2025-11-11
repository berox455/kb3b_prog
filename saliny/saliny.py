funguju = True
cas = 0
nejvetsicas = 0
predhodina = 0
nejhodina = 0
pocet_salin_now = 1   #pro vypocet nejcastejsi hodiny
pocet_salin_max = 1   #pro vypocet nejcastejsi hodiny
mezicas = 0

nsalin = int(input("Zadej pocet salin: "))

for i in range(nsalin):
    print("\nPro salinu", i+1)

    #input hodin
    while funguju:
        hodina = int(input("Zadej hodinu odjezdu: "))
    
        if hodina >= 24 or hodina < 0:
            print("Spatny format hodin!!")
        else:
            funguju = False

    funguju = True 

    #input minut
    while funguju:
        minuta = int(input("Zadej minutu odjezdu: "))
    
        if minuta >= 60 or minuta < 0:
            print("Spatny format minut!!")
        else:
            funguju = False
    
    funguju = True

    #vypis hodin
    if hodina > 10:
        if minuta < 10:
            print(i+1, ". salina odjela v ", hodina, ":0", minuta, sep="")
        else:
            print(i+1, ". salina odjela v ", hodina, ":", minuta, sep="")
    else:
        if minuta < 10:
            print(i+1, ". salina odjela v 0", hodina, ":0", minuta, sep="")
        else:
            print(i+1, ". salina odjela v 0", hodina, ":", minuta, sep="")
    

    cas = hodina*60+minuta

    #vypis a vypocet mezicasu a nejvetsiho mezicasu
    if i > 0:
        mezicas = cas - mezicas
        
        print("Cas mezi odjezdy:", mezicas, "minut")

        if mezicas >= nejvetsicas:
            nejvetsicas = mezicas

        else:
            nejvetsicas = nejvetsicas
        
        print("\nNejvetsi mezicas je:",nejvetsicas//60,"hod a", nejvetsicas%60, "min")

        mezicas = cas
    else:
        mezicas = cas

    #hodina s nejvice salinami
    if i == 0:
        predhodina = hodina
        nejhodina = hodina
    else:
        if predhodina == hodina:
            pocet_salin_now += 1
            if pocet_salin_now >= pocet_salin_max:
                nejhodina = hodina
                pocet_salin_max = pocet_salin_now
        else:
            predhodina = hodina
            pocet_salin_now = 1
    
    print("Aktualni hodina se opakovala:", pocet_salin_now)
    print("\nNejcastejsi hodinou je:", nejhodina)
    print("Pocet salin v nejcastejsi hodine:", pocet_salin_max)
    print("-------------------------------------------------------------------")