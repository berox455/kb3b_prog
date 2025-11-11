while True:
    a = float(input("\nZadej delku strany a: "))
    b = float(input("Zadej delku strany b: "))
    c = float(input("Zadej delku strany c: "))

    if a+b < c or a+c < b or b+c < a:
        print("\nTrojuhelnik nelze sestrojit!!")
    else:
        print("\nTrojuhelnik lze sestrojit")
    
    y = input("\nPokud chces overit dalsi trojuhelnik napis [y]: ")
    
    if y == "y":
        continue
    else:
        break