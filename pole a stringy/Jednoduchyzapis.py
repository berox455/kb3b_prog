#len říká délku stringu

len("Ahoj svete") #tady je len 10

"Ahoj".lower 
"Ahoj".upper #prevadi string pred nim na uppercase a lowercase

"Ahoj".isalpha
"Ahoj".isdigit # vraci bool isalpha jestli je string text a isdigit jestli je cislo

print("Ahoj"[0]) #vrati A
print("Ahoj"[3]) #vrati j
print("Ahoj"[0:]) # vrati Ahoj
print("Ahoj"[:2]) #vrati Ah
print("Ahoj"[1:3]) #vrati hoj   
print("Ahoj"[-1]) #vrati j  # string a pole muzeme indexovat, zacina to nulou


#pro pole, len() funguje i pro pole
pole = []
pole.append(2)  #prida 2
pole.remove(2)  #odstrani prvni 2
pole.sort()     #seradi pole
pole.reverse()  #obrati pole
pole.copy()     #udela kopii pole, protoze kdyz upravujeme pole ve funkci, tak upravujeme to originalni pole

#indexovani
pole[0] #prvni prvek pole
