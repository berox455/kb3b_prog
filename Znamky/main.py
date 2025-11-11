import kivy
kivy.require('2.3.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget

class ZnamkyGUI(Widget):

    znamka = 0
    vaha = 0
    i = 0

    def again(self):
        while True:
            dalsi = input("\nChces si vypocitat dalsi znamku? [a], [n]: ")

            if dalsi.lower() == "a":
                return True
            elif dalsi.lower() == "n":
                print("Doufam, ze ti tento program poslouzil dobre :)")
                return False
            else:
                print("Neco se pokazilo, nejspise si spatne zadal [a] nebo [n]\n")


    def vypocet_znamek(self):
        znamka = 0
        vaha = 0
        i = 0

        num_znamek = int(input("Zadej pocet znamek v predmetu: "))

        while i < num_znamek:
            z = float(input("Zadej znamku: "))
            v = int(input("Zadej vahu znamky: "))

            if 1 > z or z > 5 or 1 > v or v > 10:
                print("!!Zadal jsi špatně známku nebo váhu známky, zkus to znovu!!\n")
            else:
                znamka += z * v
                vaha += v
                vysledna_znamka = znamka/vaha    
                i += 1

        return vysledna_znamka


    def vypis_znamku(self, vysledna_znamka):
        print("Tvoje vysledna znamka: ", round(vysledna_znamka, 2))

        if vysledna_znamka < 1.5:
            print("Ses dobrej")

        elif vysledna_znamka < 2.5:
            print("Dvojka je supr")

        elif vysledna_znamka < 3.5:
            print("Trojec je jeste ok")

        elif vysledna_znamka < 4.5:
            print("Ctyri je jeste v klidu")

        elif vysledna_znamka <= 5:
            print("gg mas petec")

        else:
            print("bro se nauc aspon spravne zapsat znamky")


        print("---------------------------------------------------------------------------------------")


class ZnamkyApp(App):

    def build(self):
        z = ZnamkyGUI()
        while z.again():
            znamka = z.vypocet_znamek()
            z.vypis_znamku(znamka)
        
        App.get_running_app().stop()

        return z
        


if __name__ == '__main__':
    ZnamkyApp().run()
    
