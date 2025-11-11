class Bankovni_ucet():
    def __init__(self, nazev_uctu, typ_uctu, zustatek, urokova_sazba = None):
        self.nazev = nazev_uctu
        self.typ_uctu = typ_uctu.lower() #bezny nebo sporici
        self.zustatek = zustatek
        self.transakce = []
        self.vlastnik = None

        if typ_uctu.lower() == "sporici":
            self.urokova_sazba = urokova_sazba


#rozdel na funkce vklad a vyber, kde potom ty funkce pouzijes v teto funkci
    def vklad(self, penize, vypsat = True):
        if penize.isdigit() and penize > 0:
            self.vklad = penize
            
            self.zustatek += self.vklad
            self.transakce.append(self.vklad)
            if vypsat:
                print("Do vaseho uctu bylo vlozeno ", self.vklad, "Kc", sep="")
                print("---")

            return self.vklad
        else:
            print("Spatne zadane penize!!!") # more like debug


    def vyber(self, penize, vypsat = True):
        if penize.isdigit() and penize > 0 and self.typ_uctu.lower() == "bezny":
            self.vyber = penize

            if self.zustatek < self.vyber:
                print("Transakci: vybrani", self.vyber, "Kc nebylo mozne provest, protoze prevysuje vas soucasny zustatek na uctu.")
                print("---")
                self.probehla = False
                return None
            else:
                self.zustatek += self.vyber
                self.transakce.append(self.vyber)
                if vypsat:
                    print("Z vaseho uctu bylo vybrano ", self.vyber, "Kc", sep="")
                    print("---")
                return self.vyber
        elif penize.isdigit() and penize > 0:
            print("Tuto akci neni mozno provest na tomto typu uctu!!!")
            print("---")
            self.probehla = False
            return None
        else:
            print("Spatne zadane penize!!!") # more like debug

    def vklad_a_vyber(self, penize, vypsat = True):
        if penize > 0:
            self.vklad = penize

            self.zustatek += self.vklad
            self.transakce.append(self.vklad)
            if vypsat:
                print("Do vaseho uctu bylo vlozeno ", self.vklad, "Kc", sep="")
                print("---")
            return self.vklad
        elif penize < 0 and self.typ_uctu.lower() == "bezny":
            self.vyber = penize

            if self.zustatek < -self.vyber:
                print("Transakci: vybrani", self.vyber, "Kc nebylo mozne provest, protoze prevysuje vas soucasny zustatek na uctu.")
                print("---")
                self.probehla = False
                return None
            else:
                self.zustatek += self.vyber
                self.transakce.append(self.vyber)
                if vypsat:
                    print("Z vaseho uctu bylo vybrano ", self.vyber, "Kc", sep="")
                    print("---")
                return self.vyber
        else:
            print("Tuto akci neni mozno provest na tomto typu uctu!!!")
            print("---")
            self.probehla = False
            return None
    

    def uroceni(self):  #muze byt aktivovana podle urokovaciho obdobi
        self.zustatek += self.zustatek * self.urokova_sazba


    def zruseni_posledni_transakce(self, vypsat = True):
        if len(self.transakce) == 0:
            if vypsat:
                print("Nebylo mozne zrusit posledni transakci, protoze zadna transakce neprobehla")
                print("---")
            return None
        
        if self.transakce[-1] < 0:
            self.zustatek -= self.vyber
            self.prijemce.zustatek += self.vyber
        elif self.transakce[-1] > 0:
            self.zustatek -= self.vklad
            self.prijemce.zustatek += self.vklad
        else:
            return None
        
        self.transakce.remove(self.transakce[-1])
        self.prijemce.transakce = self.prijemce.transakce[:-1]

        if vypsat:
            print("Posledni transakce byla zrusena")
            print("---")


    def poslat_penize(self, kam, kolik):
        self.prijemce = kam
        self.penize = kolik
        self.probehla = True

        self.vklad_a_vyber(-self.penize, False)
        
        if self.probehla:
            self.prijemce.vklad_a_vyber(self.penize, False)
            print("Z vaseho uctu bylo poslano ", self.penize, "Kc na ", self.prijemce.nazev, sep="")
            print("---")

    
    def pridej_vlastnika(self, vlastnik):
        self.vlastnik = vlastnik
        vlastnik.ucty.append(self.nazev)


    def vypis(self):
        print("Nazev uctu:", self.nazev)
        print("Typ uctu:", self.typ_uctu)
        print("Zustatek:", self.zustatek)
        print("Historie transakci:", self.transakce)
        if self.typ_uctu.lower() == "sporici":
            print("Urokova sazba:", self.urokova_sazba)

        if self.vlastnik != None:
            print("Vlastnik:", self.vlastnik.jmeno)

        print("--------------------------------------------------")


class Klient():
    def __init__(self, jmeno, prijmeni, vek, clenstvi = "Standartni"):
        self.jmeno = jmeno
        self.prijmeni = prijmeni #bezny nebo sporici
        self.vek = vek
        self.clenstvi = clenstvi
        self.ucty = []

    
    def pridej_ucet(self, ucet):
        self.ucty.append(ucet.nazev)
        ucet.vlastnik = self


    def vypis(self):
        print("Jmeno:", self.jmeno)
        print("Prijmeni:", self.prijmeni)
        print("Vek:", self.vek)
        print("Clenstvi:", self.clenstvi)
        
        if len(self.ucty) > 0:
            print("Ucty:", self.ucty)

        print("--------------------------------------------------")

    


   
ucet1 = Bankovni_ucet("ucet1", "Bezny", 0)

ucet1.vypis()

ucet2 = Bankovni_ucet("ucet2", "Sporici", 20000, 0.03)

ucet2.vypis()
ucet2.uroceni()
ucet2.vypis()

ucet3 = Bankovni_ucet("ucet3", "bezny", 50000)

ucet3.vypis()

ucet3.poslat_penize(ucet1, 50000)

ucet3.vypis()

ucet1.poslat_penize(ucet2, 10000)

ucet1.vypis()
ucet2.vypis()
ucet3.vypis()

ucet1.poslat_penize(ucet2, 10000)

ucet1.vypis()
ucet2.vypis()
ucet3.vypis()

ucet1.zruseni_posledni_transakce()

ucet1.vypis()
ucet2.vypis()
ucet3.vypis()

aneta = Klient("Aneta", "Hodova", 30, "Premium")

aneta.vypis()

ucet1.pridej_vlastnika(aneta)
ucet2.pridej_vlastnika(aneta)
ucet3.pridej_vlastnika(aneta)

aneta.vypis()
ucet1.vypis()
ucet2.vypis()
ucet3.vypis()