while True:
    teplota = float(input("\nZadej teplotu vody: "))

    if teplota <= 0:
        print("Voda je v pevnem skupenstvi")
    elif teplota >= 100:
        print("Voda je v plynnem skupenstvi")
    else:
        print("Voda je v kapalnem skupenstvi")