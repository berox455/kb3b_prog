patra = int(input("Zadej pocet pater: "))

for i in range(patra):
    print("1", end=" ")

    for y in range(i):
        print(y+2, end=" ")
    
    print()