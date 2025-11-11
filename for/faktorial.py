num = int(input("Zadej cislo pro faktorial: "))

faktorial = 1

for i in range(num):
    i+=1
    faktorial *= i

print("Faktorial ", num, " je: ", faktorial, sep="")