num = int(input("Zadej kolik cisel chces zadat: "))

x=0

for i in range(num):
    print("Zadej ", i+1, ". cislo: ", sep="")
    x += int(input())

if num == 0:
    print("Spatny input!!")  
else:
    print("Soucet = ", x, "\nPrumer = ", x/num, sep="")