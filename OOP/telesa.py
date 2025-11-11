import math

class Ctverec():
    def __init__(self, strana, souradnice_x, souradnice_y):
        self.strana = strana
        self.souradnice = [souradnice_x, souradnice_y]

    
    def obvod(self):
        return self.strana * 4


    def obsah(self):
        return self.strana * self.strana
    

    def vypis_info(self):
        print("Ctverec", "strana v cm:", ctverec1.strana, "souradnice x, y:", ctverec1.souradnice)
        print("obvod a obsah:", ctverec1.obvod(), ctverec1.obsah())
        print("-------------------------------------------------------------------------------------------------------")

    
class Kruh():
    def __init__(self, polomer, souradnice_x, souradnice_y):
        self.polomer = polomer
        self.souradnice_stredu = [souradnice_x, souradnice_y]

    
    def prumer(self):
        return self.polomer * 2
    

    def obvod(self):
        return 2 * self.polomer * math.pi


    def obsah(self):
        return math.pi * self.polomer ** 2
    

    def vypis_info(self):
        print("Kruh", "polomer v cm:", kruh1.polomer, "souradnice stredu x, y:", kruh1.souradnice_stredu)
        print("obvod a obsah:", kruh1.obvod(), kruh1.obsah())
        print("-------------------------------------------------------------------------------------------------------")


class Pravidelny_nuhelnik():
    def __init__(self, polomer, n, souradnice_x, souradnice_y):
        self.polomer = polomer
        self.n = n
        self.souradnice_stredu = [souradnice_x, souradnice_y]

    
    def prumer(self):
        return self.polomer * 2
    
    
    def strana(self):
        return self.polomer * 2 * math.tan(math.pi/self.n)


    def obvod(self):
        return self.n * self.strana()


    def obsah(self):
        return 0.5 * self.n * self.strana() * self.polomer
    
    
    def vypis_info(self):
        print(nuhelnik1.n, "-uhlenik", " polomer v cm: ", nuhelnik1.polomer, " souradnice stredu x, y: ", nuhelnik1.souradnice_stredu, sep="")
        print("strana, obvod a obsah:", nuhelnik1.strana(), nuhelnik1.obvod() , nuhelnik1.obsah())
        print("-------------------------------------------------------------------------------------------------------")


ctverec1 = Ctverec(5, 0, 0)
#print("Ctverec", "strana v cm:", ctverec1.strana, "souradnice x, y:", ctverec1.souradnice)
#print("obvod a obsah:", ctverec1.obvod(), ctverec1.obsah())
#
#print()
#
kruh1 = Kruh(5, 0, 0)
#print("Kruh", "polomer v cm:", kruh1.polomer, "souradnice stredu x, y:", kruh1.souradnice_stredu)
#print("obvod a obsah:", kruh1.obvod(), kruh1.obsah())
#
#print()
#
nuhelnik1 = Pravidelny_nuhelnik(5, 5, 0, 0)
#print(nuhelnik1.n, "-uhlenik", " polomer v cm: ", nuhelnik1.polomer, " souradnice stredu x, y: ", nuhelnik1.souradnice_stredu, sep="")
#print("strana, obvod a obsah:", nuhelnik1.strana(), nuhelnik1.obvod() , nuhelnik1.obsah())
#
#print()

ctverec1.vypis_info()
kruh1.vypis_info()
nuhelnik1.vypis_info()
