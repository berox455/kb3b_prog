import random

class Student:
    def __init__(self, jmeno, vek, trida = None):
        self.jmeno = jmeno
        self.vek = vek
        self.trida = trida
        if trida is not None:
            trida.studenti.append(self)
        self.znamky = []


    def pridej_znamku(self, nova_znamka):
        self.znamky.append(nova_znamka)

    
    def zjisti_prumer(self):
        if len(self.znamky) == 0:
            return None
        
        soucet = 0

        for znamka in self.znamky:
            soucet += znamka

        return soucet / len(self.znamky)


    def pridej_tridu(self, nova_trida):
        if nova_trida.pocet == len(nova_trida.studenti):
            print("Trida je jiz zaplnena!!!")
            print("---")
            return None
        else:
            self.trida = nova_trida
            nova_trida.studenti.append(self)


    def zmen_tridu(self, nova_trida):   #meni tridu zaka, s tim se i smazou znamky
        if nova_trida.pocet == len(nova_trida.studenti):
            print("Trida je jiz zaplnena!!!")
            return None
        else:
            self.trida = nova_trida
            self.znamky = []
            nova_trida.studenti.append(self)


    def zmen_vek(self, novy_vek):
        self.vek = novy_vek


    def odstran_posledni_znamku(self):
        self.znamky.remove(self.znamky[-1])


    def plnoletost(self):
        return self.vek >= 18
    

    def vypis_info(self):
        print("Jmeno:", self.jmeno)
        print("Vek:", self.vek)
        print("Trida:", self.trida)
        print("Znamky:", self.znamky)
        print("Prumer:", self.zjisti_prumer())
        print("Plnoletost:", self.plnoletost())
        print("---------------------------------------------")

    
class Trida():
    def __init__(self, nazev, max_pocet_studentu):
        self.nazev = nazev
        self.pocet = max_pocet_studentu
        self.studenti = []
        self.tridni_ucitel = None
        self.zastupce_tridniho = None
        self.prumerna_znamka = None
        self.sluzba = None
    

    def pridej_tridniho(self, ucitel):
        self.tridni_ucitel = ucitel
        ucitel.trida = self


    def pridej_zastupce_tridniho(self, ucitel):
        self.zastupce_tridniho = ucitel
        ucitel.trida_zastup = self

    
    def vypocitej_prumernou_znamku(self):
        promenna = 0

        for student in self.studenti:
            if student.zjisti_prumer() is None:
                promenna = promenna #Nic nedela
            else:
                promenna += student.zjisti_prumer()

        self.prumerna_znamka = promenna / len(self.studenti)


    def zmen_sluzbu(self, student):
        self.sluzba = student


    def vypis_info(self):
        print("Nazev:", self.nazev)
        print("Kapacita studentu:", self.pocet)
        
        if self.tridni_ucitel is not None:
            print("Tridni ucitel:", self.tridni_ucitel.jmeno)

        if self.zastupce_tridniho is not None:
            print("Zastupce tridniho ucitele:", self.zastupce_tridniho.jmeno)

        if len(self.studenti) > 0:
            i = 0

            print("Studenti: ", sep="", end="")
            for student in self.studenti:
                if len(self.studenti) <= 1:
                    print(student.jmeno)
                else:
                    if i == 0:
                        print(student.jmeno, sep="", end="")
                    elif i != len(self.studenti) - 1:
                        print(", ",student.jmeno, sep="", end="")
                    else:                    
                        print(", ",student.jmeno, sep="")

                    i += 1
        
        if self.sluzba is not None:
            print("Sluzba:", self.sluzba.jmeno)
        
        if self.prumerna_znamka is not None:
            print("Prumerna znamka:", round(self.prumerna_znamka, 2))

        print("---------------------------------------------")

        

class Ucitele():
    def __init__(self, jmeno, vek, predmety = [], oducene_hodiny = 0, plat = 24000):
        self.jmeno = jmeno
        self.vek = vek
        self.predmety = predmety
        self.oducene_hodiny = oducene_hodiny
        self.trida = None
        self.trida_zastup = None
        self.zakladni_plat = plat
        self.plat = self.zakladni_plat

    
    def pridej_tridu(self, trida):
        self.trida = trida
        trida.tridni_ucitel = self


    def pridej_zastup_tridu(self, trida):
        self.trida_zastup = trida
        trida.zastupce_tridniho = self


    def spocitej_vyplatu(self, bonus = 0):
        if self.trida is not None:


            self.plat += len(self.trida.studenti) * 200

            for student in self.trida.studenti:
                if student.zjisti_prumer() < 2.5 and student.zjisti_prumer() is not None:
                    self.plat += 75

            if self.oducene_hodiny > 200:
                self.plat += (self.oducene_hodiny-200) * 30

        if self.trida_zastup is not None:
            self.plat += 2000

        self.plat += bonus

        return self.plat




    def vypis_info(self):
            print("Jmeno:", self.jmeno)
            print("Vek:", self.vek)
            print("Predmety:", self.predmety)
            print("Oducene hodiny: ", self.oducene_hodiny, "h", sep="")
            
            if self.trida is not None:
                print("Trida:", self.trida.nazev)

            if self.trida_zastup is not None:
                print("Zastupni trida:", self.trida_zastup.nazev)

            print("Zakladni plat: ",self.zakladni_plat, "Kc", sep="")

            if self.plat != self.zakladni_plat:
                print("Plat po pridani bonusu: ",self.plat, "Kc", sep="")

            print("---------------------------------------------")


class Pracovnik():
    def __init__(self, jmeno, prijmeni, plat, pracovni_doba = [9,17]):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.plat = plat
        self.pracovni_doba = pracovni_doba
        self.patro = None
        self.povolani = None

    
    def pridej_povolani(self, povolani):
        self.povolani = povolani
    

    def prirad_patro(self, patro):
        self.patro = patro


    def vypis(self):
        print("Pracovnik:")
        print("Jmeno:", self.jmeno)
        print("Prijmeni:", self.prijmeni)
        print("Plat:", self.plat)
        print("Pracovni doba: od", self.pracovni_doba[0], "do", self.pracovni_doba[1])
        
        if self.povolani != None:
            print("S povolanim:", self.povolani)
        
        if self.patro != None:
            print("Ma patro:", self.patro)

        print("---------------------------------------------")

student1 = Student("Bořivoj", 14)
student2 = Student("Alenka", 16)
student3 = Student("Bohumil", 18)
student4 = Student("Karel", 18)


#student1.vypis_info()
#student2.vypis_info()
#student3.vypis_info()
student4.vypis_info()


kb3b = Trida("KB3B", 30)
kb3b.vypis_info()

hradkova = Ucitele("Hradkova", 70, ["prava", "obcanka", "rustina"], 10000, 25000)
hradkova.vypis_info()

kb3b.pridej_tridniho(hradkova)

kb3b.vypis_info()
hradkova.vypis_info()

pracovnik = Pracovnik("Borec", "Janku", 22000)

pracovnik.vypis()

pribylova = Ucitele("Pribylova", 70, ["cestina"], 5000, 24000)

pribylova.vypis_info()

kb3b.vypis_info()

student1.pridej_tridu(kb3b)
student2.pridej_tridu(kb3b)
student3.pridej_tridu(kb3b)
student4.pridej_tridu(kb3b)

kb3b.vypis_info()

student1.pridej_znamku(1)
student1.pridej_znamku(1)
student1.pridej_znamku(1)
student1.pridej_znamku(1)
student1.pridej_znamku(5)

student2.pridej_znamku(1)
student2.pridej_znamku(1)
student2.pridej_znamku(1)
student2.pridej_znamku(1)

student3.pridej_znamku(1)
student3.pridej_znamku(1)
student3.pridej_znamku(1)
student3.pridej_znamku(1)

student4.pridej_znamku(1)
student4.pridej_znamku(1)
student4.pridej_znamku(1)
student4.pridej_znamku(1)

kb3b.vypocitej_prumernou_znamku()

kb3b.vypis_info()

kb3b.pridej_zastupce_tridniho(pribylova)
kb3b.vypis_info()

kb3b.zmen_sluzbu(student1)
kb3b.vypis_info()

#Vytvareni studentu
student5 = Student("Anna", 22, kb3b)
student6 = Student("Jakub", 21, kb3b)
student7 = Student("Tereza", 23, kb3b)
student8 = Student("Petr", 24, kb3b)
student9 = Student("Lucie", 22, kb3b)
student10 = Student("Martin", 23, kb3b)
student11 = Student("Karla", 21, kb3b)
student12 = Student("David", 20, kb3b)
student13 = Student("Eva", 25, kb3b)
student14 = Student("Jana", 24, kb3b)
student15 = Student("Tomáš", 23, kb3b)
student16 = Student("Simona", 22, kb3b)
student17 = Student("Vojtěch", 20, kb3b)
student18 = Student("Petra", 21, kb3b)
student19 = Student("Jan", 23, kb3b)
student20 = Student("Michaela", 24, kb3b)
student21 = Student("Ondřej", 25, kb3b)
student22 = Student("Barbora", 21, kb3b)
student23 = Student("František", 22, kb3b)
student24 = Student("Martina", 23, kb3b)
student25 = Student("Radek", 24, kb3b)
student26 = Student("Veronika", 25, kb3b)
student27 = Student("Filip", 21, kb3b)
student28 = Student("Klára", 20, kb3b)
student29 = Student("Alena", 22, kb3b)
student30 = Student("Roman", 23, kb3b)
student31 = Student("Helena", 24)

kb3b.vypis_info()

student31.pridej_tridu(kb3b)

kb3b.zmen_sluzbu(random.choice(kb3b.studenti))
kb3b.vypis_info()


#Pridavani znamek studentum
student5.pridej_znamku(random.randint(1, 5))
student6.pridej_znamku(random.randint(1, 5))
student7.pridej_znamku(random.randint(1, 5))
student8.pridej_znamku(random.randint(1, 5))
student9.pridej_znamku(random.randint(1, 5))
student10.pridej_znamku(random.randint(1, 5))
student11.pridej_znamku(random.randint(1, 5))
student12.pridej_znamku(random.randint(1, 5))
student13.pridej_znamku(random.randint(1, 5))
student14.pridej_znamku(random.randint(1, 5))
student15.pridej_znamku(random.randint(1, 5))
student16.pridej_znamku(random.randint(1, 5))
student17.pridej_znamku(random.randint(1, 5))
student18.pridej_znamku(random.randint(1, 5))
student19.pridej_znamku(random.randint(1, 5))
student20.pridej_znamku(random.randint(1, 5))
student21.pridej_znamku(random.randint(1, 5))
student22.pridej_znamku(random.randint(1, 5))
student23.pridej_znamku(random.randint(1, 5))
student24.pridej_znamku(random.randint(1, 5))
student25.pridej_znamku(random.randint(1, 5))
student26.pridej_znamku(random.randint(1, 5))
student27.pridej_znamku(random.randint(1, 5))
student28.pridej_znamku(random.randint(1, 5))
student29.pridej_znamku(random.randint(1, 5))
student30.pridej_znamku(random.randint(1, 5))
student31.pridej_znamku(random.randint(1, 5))
student5.pridej_znamku(random.randint(1, 5))
student6.pridej_znamku(random.randint(1, 5))
student7.pridej_znamku(random.randint(1, 5))
student8.pridej_znamku(random.randint(1, 5))
student9.pridej_znamku(random.randint(1, 5))
student10.pridej_znamku(random.randint(1, 5))
student11.pridej_znamku(random.randint(1, 5))
student12.pridej_znamku(random.randint(1, 5))
student13.pridej_znamku(random.randint(1, 5))
student14.pridej_znamku(random.randint(1, 5))
student15.pridej_znamku(random.randint(1, 5))
student16.pridej_znamku(random.randint(1, 5))
student17.pridej_znamku(random.randint(1, 5))
student18.pridej_znamku(random.randint(1, 5))
student19.pridej_znamku(random.randint(1, 5))
student20.pridej_znamku(random.randint(1, 5))
student21.pridej_znamku(random.randint(1, 5))
student22.pridej_znamku(random.randint(1, 5))
student23.pridej_znamku(random.randint(1, 5))
student24.pridej_znamku(random.randint(1, 5))
student25.pridej_znamku(random.randint(1, 5))
student26.pridej_znamku(random.randint(1, 5))
student27.pridej_znamku(random.randint(1, 5))
student28.pridej_znamku(random.randint(1, 5))
student29.pridej_znamku(random.randint(1, 5))
student30.pridej_znamku(random.randint(1, 5))
student31.pridej_znamku(random.randint(1, 5))

kb3b.vypocitej_prumernou_znamku()
kb3b.vypis_info()

hradkova.spocitej_vyplatu(200)
pribylova.spocitej_vyplatu(1000)

hradkova.vypis_info()
pribylova.vypis_info()