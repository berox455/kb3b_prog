while True:
    prijem = float(input("\nZadej vysi prijmu: "))

    prijem -= 10000
    dan = 0.0

    if prijem <= 0:
        print("Neplatis dane")
    elif prijem - 20000 <= 0:
        dan = prijem * 0.1
        print("Platis dan:", dan, "Kc", sep="")
    else:
        prijem -= 20000
        dan = prijem * 0.25 + 2000
        print("Platis dan: ", dan, "Kc", sep="")