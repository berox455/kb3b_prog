import math

r = float(input("Zadej polomer valce: "))
v = float(input("Zadej vysku valce: "))

S = 2*math.pi*r*(r+v)

print("Povrch valce: ", S)