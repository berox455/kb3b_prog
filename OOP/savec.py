class Savec:
    def __init__(self, jmeno, hmotnost):
        self.jmeno = jmeno
        self.hmotnost = hmotnost

    
    def snez(self, jidlo):
        print(self.jmeno, "snedl", jidlo)


class Kocka(Savec):
    def __init__(self, jmeno, hmotnost, majitel):
        super().__init__(jmeno, hmotnost)
        self.majitel = majitel


    def ulov_mys(self):
        print(self.jmeno, "ulovila mys")


    def zmen_majitele(self, majitel):
        self.majitel = majitel
        print(self.jmeno, "zmenila majitele na", self.majitel)


kocka = Kocka("kocka", 2000, "Lukas")
kocka.ulov_mys()
kocka.snez("mys")
kocka.zmen_majitele("Lenka")